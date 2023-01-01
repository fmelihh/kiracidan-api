import traceback
import bcrypt

from ...db.postgres import transaction_scope
from ...models import User
from ...schemes.user import UserScheme
from ...core.auth import Handler, HandlerPayloadResponse, EncodedTokenResponse, DecodedTokenResponse


def register(user_credentials: UserScheme):
    try:
        with transaction_scope() as session:
            is_usr_exists = session.query(User).filter(User.email == user_credentials.email).first()
            if is_usr_exists:
                raise Exception("User already exists.")

            user_credentials.password = bcrypt.hashpw(user_credentials.password.encode("utf-8"), bcrypt.gensalt())
            user_credentials = user_credentials.dict()
            user_object = User(**user_credentials)
            session.add(user_object)

    except Exception as e:
        traceback.print_exc()
        raise e


def login(email: str, password: str) -> EncodedTokenResponse:
    try:
        with transaction_scope() as session:
            user = session.query(User).filter(User.email == email).first()
            if not user or not bcrypt.checkpw(password.encode("utf-8"), user.password):
                raise Exception("User doesn't exists")

            payload = HandlerPayloadResponse(
                handler_name="token_generate",
                role_type=user.role.role_name,
                user_info=DecodedTokenResponse(
                    token_type=user.role.role_name,
                    email=user.email
                )
            )
            encoded_token = Handler().handle(payload=payload)

        return encoded_token
    except Exception as e:
        traceback.print_exc()
        raise e


import traceback
from jose import jwt
from dynaconf import settings
import datetime

from .abstract import  AbstractHandler
from .token_response import HandlerPayloadResponse, DecodedTokenResponse, EncodedTokenResponse

class TokenGenerationHandler(AbstractHandler):
    _next_handler = None

    def handle(self, payload: HandlerPayloadResponse) -> EncodedTokenResponse:
        try:
            encoded_token_response = TokenGenerationHandler.encode_token(payload.role_type, **payload.params)
            return encoded_token_response
        except Exception as e:
            traceback.print_exc()
            raise e

    @staticmethod
    def encode_token(role_type: str, user_info: DecodedTokenResponse) -> EncodedTokenResponse:
        try:
            if role_type != user_info.token_type:
                raise Exception("Roles did not match.")
            expires_delta = datetime.datetime.utcnow() + datetime.timedelta(minutes=settings.TOKEN_EXPIRED_MINUTES)
            to_encode = dict(exp=expires_delta, sub=str(user_info.to_dict()))
            token = jwt.encode(to_encode, settings.TOKEN_SECRET, settings.TOKEN_ALGORITHM)
            return EncodedTokenResponse(token=token)
        except Exception as e:
            raise e

import traceback
from jose import JWTError, jwt
import json
from dynaconf import settings
import datetime

from .token_response import  HandlerPayloadResponse, DecodedTokenResponse, EncodedTokenResponse
from .abstract import AbstractHandler

class TokenDecodeHandler(AbstractHandler):
    _next_handler = None
    def handle(self, payload: HandlerPayloadResponse) -> DecodedTokenResponse:
        try:
             decoded_token_response = TokenDecodeHandler.decode_token(payload.role_type, **payload.params)
             return decoded_token_response
        except Exception as e:
            traceback.print_exc()
            raise e

    @staticmethod
    def decode_token(role_type: str, encoded_token: EncodedTokenResponse) -> DecodedTokenResponse:
        try:
            payload = jwt.decode(str(encoded_token.token), settings.TOKEN_SECRET, algorithms=[settings.TOKEN_ALGORITHM])
            exp = payload.pop("exp")
            if datetime.datetime.fromtimestamp(exp) < datetime.datetime.now():
                raise Exception("Token expired.")

            data = json.loads(payload["sub"].replace("'", '"'))
            user_info = DecodedTokenResponse(**data)
            if user_info.token_type != role_type:
                raise Exception("Roles did not match.")

            return user_info
        except JWTError as e:
            raise e
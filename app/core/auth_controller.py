from fastapi import Security
from fastapi.security.api_key import APIKeyHeader

from .auth import HandlerPayloadResponse, Handler, EncodedTokenResponse


class AuthController:
    def __init__(self, token: str = Security(APIKeyHeader(name="auth"))):
        encoded_token = EncodedTokenResponse(token=token)
        self.user_credentials = Handler().handle(
            payload=HandlerPayloadResponse(
                handler_name="token_decode",
                encoded_token=encoded_token
            )
        )

    def to_dict(self):
        return self.user_credentials.to_dict()

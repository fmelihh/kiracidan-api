from .abstract import AbstractEncodedTokenResponse, AbstractDecodedTokenResponse, AbstractHandlerPayload


class HandlerPayloadResponse(AbstractHandlerPayload):
    def __init__(self, handler_name: str, role_type: str = None, **kwargs):
        self.handler_name = handler_name
        self.role_type: str = role_type
        self.params = kwargs
    def to_dict(self):
        return {
            "handler_name": self.handler_name,
            "role_type": self.role_type,
            "params": self.params
        }


class EncodedTokenResponse(AbstractEncodedTokenResponse):
    def __init__(self, token: str):
        self.token = token

    def to_dict(self):
        return {
            "token": self.token
        }


class DecodedTokenResponse(AbstractDecodedTokenResponse):
    def __init__(self, email: str, token_type: str):
        self.email = email
        self.token_type = token_type

    def to_dict(self):
        return {
            "email": self.email,
            "token_type": self.token_type,
        }

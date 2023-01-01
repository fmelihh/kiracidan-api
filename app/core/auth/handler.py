import traceback
from typing import Any
from .token_response import HandlerPayloadResponse
from .abstract import AbstractHandler

from .token_decoder_handler import TokenDecodeHandler
from .token_generator_handler import TokenGenerationHandler
from .token_role_check_handler import TokenRoleCheckHandler


class Handler(AbstractHandler):
    _next_handler = {
        "token_generate": TokenGenerationHandler,
        "token_decode": TokenDecodeHandler,
        "token_check_role": TokenRoleCheckHandler
    }

    def handle(self, payload: HandlerPayloadResponse) -> Any:
        try:
            next_object = self._next_handler.get(payload.handler_name)
            if next_object is None:
                raise Exception("An error occurred. Handler not found.")

            payload.handler_name = payload.role_type.upper() if payload.role_type else payload.role_type
            response = next_object().handle(payload=payload)
            return response
        except Exception as e:
            traceback.print_exc()
            raise e



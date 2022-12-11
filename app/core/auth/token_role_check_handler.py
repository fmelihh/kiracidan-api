import traceback

from .abstract import  AbstractHandler
from .token import TenantRole, HomeOwnerRole
from .token_response import HandlerPayloadResponse
class TokenRoleCheckHandler(AbstractHandler):
    _next_handler = {
        TenantRole.ROLE: TenantRole,
        HomeOwnerRole.ROLE: HomeOwnerRole
    }

    def handle(self, payload: HandlerPayloadResponse):
        try:
            next_obj = self._next_handler.get(payload.role_type)
            if next_obj is None:
                raise Exception("An error occurred. Handler not found.")

            payload.handler_name = "check_scope"
            next_obj().handle(payload=payload)
        except Exception as e:
            traceback.print_exc()
            raise e
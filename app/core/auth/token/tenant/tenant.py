from ...token_response import HandlerPayloadResponse
from ...abstract import AbstractToken, AbstractHandler
from ...constants import TENANT_ROLE
class TenantRole(AbstractHandler, AbstractToken):
    _next_handler = None
    ROLE = TENANT_ROLE

    def handle(self, payload: HandlerPayloadResponse):
        response = getattr(self, payload.handler_name)(**payload.params)
        return response

    def check_scope(self, scope: str) -> bool:
        print("tenant check scope çalıştı")
        return True
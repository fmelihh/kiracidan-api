from ...token_response import HandlerPayloadResponse
from ...abstract import AbstractToken, AbstractHandler
from ...constants import HOME_OWNER_ROLE
class HomeOwnerRole(AbstractHandler, AbstractToken):
    _next_handler = None
    ROLE = HOME_OWNER_ROLE

    def handle(self, payload: HandlerPayloadResponse):
        response = getattr(self, payload.handler_name)(**payload.params)
        return response

    def check_scope(self, scope: str) -> bool:
        print("home owner check scope çalıştı")
        return True

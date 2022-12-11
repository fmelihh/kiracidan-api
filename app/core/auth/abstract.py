from typing import Any
from abc import ABC, abstractmethod

class AbstractHandlerPayload(ABC):
    @abstractmethod
    def to_dict(self):
        ...

class AbstractHandler(ABC):
    _next_handler = NotImplementedError
    @abstractmethod
    def handle(self, payload: AbstractHandlerPayload) -> Any:
        ...

class AbstractDecodedTokenResponse(ABC):
    @abstractmethod
    def to_dict(self):
        ...
class AbstractEncodedTokenResponse(ABC):
    @abstractmethod
    def to_dict(self):
        ...

class AbstractToken(ABC):
    token_type = NotImplementedError
    @abstractmethod
    def check_scope(self, scope: str) -> bool:
        ...
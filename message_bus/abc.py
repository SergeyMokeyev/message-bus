from abc import ABC, abstractmethod
from typing import Union, List, AsyncGenerator
from message_bus.dsn import DSN


class Message(ABC):
    @property
    @abstractmethod
    def channel(self) -> str:
        pass

    @abstractmethod
    def serialize(self) -> bytes:
        pass

    @classmethod
    @abstractmethod
    def deserialize(cls, data: bytes) -> 'Message':
        pass


class MessageBus(ABC):
    def __init__(self, dsn: DSN):
        self.dsn = dsn

    @abstractmethod
    async def connect(self):
        pass

    @abstractmethod
    async def disconnect(self):
        pass

    @abstractmethod
    async def send(self, message: Message) -> None:
        pass

    @abstractmethod
    async def receive(self, message: Union[Message, List[Message]]) -> AsyncGenerator[Message, None]:
        pass

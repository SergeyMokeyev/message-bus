from enum import Enum
from typing import AsyncGenerator, List, Union
from message_bus.dsn import DSN
from message_bus.abc import Message
from message_bus.redis import RedisMessageBus


class MessageBusEnum(Enum):
    redis = RedisMessageBus


class MessageBusClient:
    def __init__(self, dsn: str):
        self.dsn = DSN.parse(dsn)
        self.__message_bus = MessageBusEnum[self.dsn.schema].value(self.dsn)

    async def send(self, message: Message) -> None:
        pass

    async def receive(self, message: Union[Message, List[Message]],
                      *, status: Union[str, List[str]] = None) -> AsyncGenerator:
        pass

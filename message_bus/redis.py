from typing import Union, List, AsyncGenerator
from message_bus.abc import MessageBus, Message
from aredis import StrictRedisCluster


class RedisMessageBus(MessageBus):
    async def connect(self):
        pass

    async def disconnect(self):
        pass

    async def send(self, message: Message) -> None:
        pass

    async def receive(self, message: Union[Message, List[Message]]) -> AsyncGenerator:
        pass

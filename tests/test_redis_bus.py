from unittest import IsolatedAsyncioTestCase
from message_bus import MessageBusClient


class TestSendAndReceive(IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.m_bus = MessageBusClient('redis://127.0.0.1:6379')
        msg_bus = ''

    async def asyncTearDown(self):
        pass

    async def test_send_and_receive(self):
        await self.m_bus.send('')

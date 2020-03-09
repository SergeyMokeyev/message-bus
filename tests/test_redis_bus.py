from unittest import IsolatedAsyncioTestCase


class TestSendAndReceive(IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        pass

    async def asyncTearDown(self):
        pass

    async def test_send_and_receive(self):
        print(11)

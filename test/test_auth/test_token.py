import time
from unittest import TestCase

from app.core.auth import TokenGenerator


class TestToken(TestCase):
    def setUp(self) -> None:
        self.message = {"msg": "HelloWorld"}
        self.app = TokenGenerator(message=self.message)

    def test_generate_token(self):
        self.app.exp = 9999
        token = self.app.generate_token()

        self.assertIsInstance(token, str)

    def test_decode_token(self):
        self.app.exp = 9999
        token = self.app.generate_token()
        msg = self.app.decode_token(token=token)

        self.assertEqual(msg, self.message)

    def test_generate_token_expired(self):
        self.app.exp = 1
        token = self.app.generate_token()
        time.sleep(2)

        msg = self.app.decode_token(token=token)
        self.assertEqual(msg, {"msg": "Token expired"})



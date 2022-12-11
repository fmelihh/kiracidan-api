from app.core.auth import HOME_OWNER_ROLE, TENANT_ROLE, Handler, HandlerPayloadResponse, EncodedTokenResponse, DecodedTokenResponse
from unittest import TestCase

class TestAuthentication(TestCase):
    def setUp(self) -> None:
        self.handler = Handler()

    def test_encode_token(self):
        navigator = "token_generate"
        token: EncodedTokenResponse = self.handler.handle(payload=HandlerPayloadResponse(
            handler_name=navigator,
            role_type=TENANT_ROLE,
            user_info=DecodedTokenResponse(
                email="test_blabla",
                token_type=TENANT_ROLE
            )
        ))
        print(token.to_dict())
        self.assertIn("token", token.to_dict())
        self.assertIsInstance(token.token, str)
    def test_decode_token(self):
        navigator = "token_decode"
        user_info: DecodedTokenResponse = self.handler.handle(payload=HandlerPayloadResponse(
            handler_name=navigator,
            role_type=TENANT_ROLE,
            encoded_token=EncodedTokenResponse(
                token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NzA4MDEyNzgsInN1YiI6InsnZW1haWwnOiAndGVzdF9ibGFibGEnLCAndG9rZW5fdHlwZSc6ICdURU5BTlQnfSJ9.GC4HGGJnDstZMbdl0BSPgSTFdGIhwgeaQphJALuIR4I'
            )
        ))
        print(user_info.to_dict())
        self.assertIn("email", user_info.to_dict())
        self.assertIn("token_type", user_info.to_dict())
        self.assertIsInstance(user_info.to_dict()["email"], str)
        self.assertIsInstance(user_info.to_dict()["token_type"], str)


    def test_check(self):
        pass
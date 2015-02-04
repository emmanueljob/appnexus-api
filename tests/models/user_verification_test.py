import unittest
import json

from appnexusclient.models.user_verification import UserVerification
from tests.base import Base


class UserVerificationTest(Base):

    def testCreateAndVerify(self):
        user_info = UserVerification(UserVerificationTest.conn)
        token = user_info.create_token()
        assert token is not None

        loader = UserVerification(UserVerificationTest.conn)
        user_id = loader.get_user_id(token)
        assert user_id is not None

    def testGetAuthorization(self):
        user_info = UserVerification(UserVerificationTest.conn)
        auth_token = user_info.get_authorization(7720)
        assert auth_token is not None

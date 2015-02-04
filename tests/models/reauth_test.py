import unittest
import json

from appnexusclient.models.profile import Profile
from appnexusclient.service.connection import Connection
from tests.base import Base


class ReauthTest(Base):

    def testReauth(self):
        Connection.tmp_file = '/tmp/auth_test.txt'
        tmp_file = open(Connection.tmp_file, 'w')
        tmp_file.write('bad_token')

        profile_id = 423662
        advertiser_id = 136402
        loader = Profile(ReauthTest.conn)
        profile = loader.find_one(profile_id, advertiser_id)

        assert profile is not None

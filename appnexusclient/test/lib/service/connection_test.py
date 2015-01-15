import unittest

from appnexusclient.conf.properties import Properties
from appnexusclient.lib.service.connection import Connection
from appnexusclient.test.lib.base import Base


class ConnectionTest(Base):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGetProps(self):
        assert self.username == "accuen_ct_api_user"

    def testConnection(self):
        token = ConnectionTest.conn.authorize()
        assert token is not None

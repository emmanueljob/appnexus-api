import unittest

from conf.properties import Properties
from lib.service.connection import Connection
from tests.lib.base import Base


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

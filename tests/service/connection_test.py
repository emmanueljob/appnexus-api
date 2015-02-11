import os
import unittest

from appnexusclient.conf.properties import Properties
from appnexusclient.service.connection import Connection
from tests.base import Base


class ConnectionTest(Base):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGetProps(self):
        assert self.username == "emmanuel.job@accuenmedia.com"

    def testConnection(self):
        token = ConnectionTest.conn.authorize()
        assert token is not None

    def testConnectionTmpFile(self):
        Connection.tmp_file = '/tmp/auth_test.txt'
        token = ConnectionTest.conn.authorize()
        assert token is not None

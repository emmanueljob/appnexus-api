import unittest

from appnexusclient.conf.properties import Properties
from appnexusclient.service.connection import Connection


class Base(unittest.TestCase):

    conn = None

    def __init__(self, *args, **kwargs):

        props = Properties("test")
        self.username = props.username
        self.password = props.password
        self.url = props.url
        Base.conn = Connection(username=self.username,
                               password=self.password,
                               url=self.url)

        Connection.tmp_file = '/tmp/test_auth.txt'

        super(Base, self).__init__(*args, **kwargs)

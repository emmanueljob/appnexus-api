import unittest
import json

from appnexusclient.models.publisher import Publisher
from tests.base import Base


class PublisherTest(Base):

    def testCreate(self):
        publisher = Publisher(PublisherTest.conn)
        publisher['name'] = 'publisher test from python test'
        result = publisher.create()
        assert result == publisher.get('id')

    def testGet(self):
        loader = Publisher(PublisherTest.conn)
        publishers = loader.find()
        for publisher in publishers:
            assert publisher.get('id') is not None

    def testGetById(self):
        publisher_id = 169322
        loader = Publisher(PublisherTest.conn)
        publisher = loader.find(publisher_id)
        assert publisher_id == publisher.get('id')

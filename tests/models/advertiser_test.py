import unittest
import json

from appnexusclient.models.advertiser import Advertiser
from tests.base import Base


class AdvertiserTest(Base):

    def testGet(self):
        loader = Advertiser(AdvertiserTest.conn)
        advs = json.loads(loader.find())
        for adv in advs.get('data').get('response').get('advertisers'):
            assert adv.get('name') is not None

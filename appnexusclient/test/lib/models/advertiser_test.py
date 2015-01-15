import unittest
import json

from appnexusclient.lib.models.advertiser import Advertiser
from appnexusclient.test.lib.base import Base


class AdvertiserTest(Base):

    def testGet(self):
        loader = Advertiser(AdvertiserTest.conn)
        advs = loader.find()
        for adv in advs:
            assert adv.get('name') is not None

import unittest
import json

from lib.models.advertiser import Advertiser
from tests.lib.base import Base


class AdvertiserTest(Base):

    def testGet(self):
        loader = Advertiser(AdvertiserTest.conn)
        advs = loader.find()
        for adv in advs:
            assert adv.get('name') is not None

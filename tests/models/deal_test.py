import unittest
import json

from appnexusclient.models.deal import Deal
from tests.base import Base


class DealTest(Base):

    def testGet(self):
        loader = Deal(DealTest.conn)
        deals = json.loads(loader.find())
        for deal in deals.get('data').get('response').get('deals'):
            assert deal.get('id') is not None

    def testGetById(self):
        deal_id = 6007
        loader = Deal(DealTest.conn)
        deal = json.loads(loader.find(deal_id))
        assert deal_id == deal.get('data').get('response').get('deal').get('id')

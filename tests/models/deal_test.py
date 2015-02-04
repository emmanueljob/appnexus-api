import unittest
import json

from appnexusclient.models.deal import Deal
from tests.base import Base


class DealTest(Base):

    def testCreate(self):
        deal = Deal(DealTest.conn)
        deal.set_buyer(4091)
        deal['name'] = 'python test deal'
        deal['floor_price'] = 1.0
        result = deal.create()
        assert result == deal.get('id')

    def testGet(self):
        loader = Deal(DealTest.conn)
        deals = loader.find()
        for deal in deals:
            assert deal.get('id') is not None

    def testGetById(self):
        deal_id = 2000
        loader = Deal(DealTest.conn)
        deal = loader.find(deal_id)
        assert deal_id == deal.get('id')

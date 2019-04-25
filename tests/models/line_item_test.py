import json
import unittest

from appnexusclient.models.line_item import LineItem
from tests.base import Base


class LineItemTest(Base):

    def testSearch(self):
        adv_id = 482212

        loader = LineItem(LineItemTest.conn)
        line_items = loader.find_by_advertiser(adv_id)

        assert len(line_items) > 1


    def testSearchByInsertionOrder(self):
        adv_id = 482212
        io_id = 1030212

        loader = LineItem(LineItemTest.conn)
        line_items = loader.find_by_insertion_order(adv_id, io_id)

        for line_item in line_items:
            print(json.dumps(line_item, indent=2))

        assert len(line_items) > 0

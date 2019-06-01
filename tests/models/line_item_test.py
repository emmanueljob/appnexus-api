import json
import unittest

from appnexusclient.models.line_item import LineItem
from tests.base import Base


class LineItemTest(Base):

    def testSearch(self):
        adv_id = 482212

        loader = LineItem(LineItemTest.conn)
        line_items = json.loads(loader.find_by_advertiser(adv_id))
        for li in line_items.get('data').get('response').get('line-items'):
            assert li.get('id') > 1
            assert li.get('advertiser').get('id') == adv_id


    def testSearchByInsertionOrder(self):
        adv_id = 482212
        io_id = 1030212

        loader = LineItem(LineItemTest.conn)
        line_items = json.loads(loader.find_by_insertion_order(adv_id, io_id))

        for li in line_items.get('data').get('response').get('line-items'):
            assert li.get('advertiser').get('id') == adv_id
            found = False
            for io in li.get('insertion_orders'):
                if io.get('id') == io_id:
                    found = True
            if not found:
                assert "IO NOT FOUND" == "FOR THIS LI"

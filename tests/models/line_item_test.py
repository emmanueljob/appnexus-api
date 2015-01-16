import unittest

from appnexusclient.models.line_item import LineItem
from tests.base import Base


class LineItemTest(Base):

    def testSearch(self):
        adv_id = 136482

        loader = LineItem(LineItemTest.conn)
        line_items = loader.find_by_advertiser(adv_id)

        assert len(line_items) > 1

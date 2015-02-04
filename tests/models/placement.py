import unittest
import json

from appnexusclient.models.placement import Placement
from tests.base import Base


class PlacementTest(Base):

    def testCreate(self):
        placement = Placement(PlacementTest.conn)
        placement['name'] = 'placement test'
        placement['publisher_id'] = 169322
        result = placement.create()
        assert result == placement.get('id')
        
    def testGet(self):
        loader = Placement(PlacementTest.conn)
        placements = loader.find()
        for placement in placements:
            assert placement.get('id') is not None

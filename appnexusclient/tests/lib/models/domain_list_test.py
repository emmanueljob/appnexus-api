import unittest
import json
import random

from lib.models.domain_list import DomainList
from tests.lib.base import Base


class DomainListTest(Base):

    def testCreate(self):
        d_list = DomainList(DomainListTest.conn)
        d_list['name'] = "domain list test"
        d_list['description'] = "domain list test description"
        d_list['domains'] = ['www.espn.com', 'www.cnn.com']
        result = d_list.create()
        assert result == d_list.get('id')

    def testSearch(self):
        rand = random.randint(1, 100000)

        name = "domain list test " + str(rand)

        d_list = DomainList(DomainListTest.conn)
        d_list['name'] = name
        d_list['description'] = "domain list test description"
        d_list['domains'] = ['www.espn.com', 'www.cnn.com']
        result = d_list.create()
        assert result == d_list.get('id')

        loader = DomainList(DomainListTest.conn)
        d_list_found = loader.find_by_name(name)

        assert d_list.get('id') == d_list_found.get('id')

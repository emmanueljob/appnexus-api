import json
import unittest

from appnexusclient.models.inventory_list_item import InventoryListItem
from appnexusclient.models.inventory_list import InventoryList
from tests.data.domains import get_domains
from tests.base import Base


class InventoryListItemTest(Base):

    def testSearch(self):
        adv_id = 482212

#        inventory_list = InventoryList(InventoryListItemTest.conn)
#        inventory_list['name'] = 'unit test'
#        inventory_list['inventory_list_type'] = 'whitelist'
#
#        response = json.loads(inventory_list.create())
#        data = response.get('data').get('response').get('inventory-list')
#
#        print "data",data
#        return 

        data = {'id':  23601}
        InventoryListItem(InventoryListItemTest.conn, data)

        inventory_list_item = InventoryListItem(InventoryListItemTest.conn, data)
        
        domains = get_domains()
        print domains[0]
        cleaned = []
        for domain in domains:
            cleaned.append(domain['url'])
        inventory_list_item.set_domains(cleaned)
        response = inventory_list_item.save()
        print response

        #assert len(line_items) > 1


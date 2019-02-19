import unittest
import json

from appnexusclient.models.line_item import LineItem
from appnexusclient.models.inventory_list import InventoryList
from appnexusclient.models.inventory_list_item import InventoryListItem
from appnexusclient.models.profile import Profile
from tests.base import Base


class NewSyncTest(Base):

    def testRunSync(self):
        adv_id = 482212
        id = 7292865
        profile_id = 109369442
        inventory_list_id = 23639

        loader = LineItem(NewSyncTest.conn)
        line_item = loader.find_one(id, adv_id)

        line_item =  json.loads(line_item)['data']['response']['line-item']
        print json.dumps(line_item, indent=2)

        loader = Profile(NewSyncTest.conn)
        profile = loader.find_one(profile_id, adv_id)

        profile =  json.loads(profile)['data']['response']['profile']
        print json.dumps(profile, indent=2)


        loader = InventoryList(NewSyncTest.conn)
        inventory_list = loader.find_by_id(inventory_list_id)
        
        inventory_list =  json.loads(inventory_list)['data']['response']['inventory-lists'][0]
        print json.dumps(inventory_list, indent=2)

        loader = InventoryListItem(NewSyncTest.conn)
        inventory_list_items = loader.find_by_list_id(inventory_list['id'])
        print inventory_list_items

        loader = InventoryListItem(NewSyncTest.conn, {'id': inventory_list['id']})
        loader.set_domains(['www.espn.com', 'eman.com', 'e-man.com'])
        print loader.save()
        
        

        
        

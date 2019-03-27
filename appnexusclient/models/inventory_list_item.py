import json

from appnexusclient.models.base import Base

class InventoryListItem(Base):

    obj_name = "inventory-list"

    def set_domains(self, domains):

        # Verify the domains first and use what is returned
        to_post = {'inventory-items': [{'url': domain} for domain in domains]}
        url = "{0}/{1}".format(self.get_url(), 'validate-inventory-item')
        response = json.loads(self._execute("POST", url, json.dumps(to_post)).text)

        # no valid domains to save
        if not response.get('response') or \
                not response.get('response').get('inventory-items'):
            return 

        domains_to_save = set()
        for d in response.get('response').get('inventory-items'):
            if d.get('is_valid'):
                domains_to_save.add(d.get('inventory_url'))

        self.data["inventory-list-items"] = []

        for domain in domains_to_save:
            row = {
                "url": domain,
                "include_children": False
            }
            self.data["inventory-list-items"].append(row)

    def get_save_url(self, id, advertiser_id=None):
        return "{0}/{1}/item".format(self.get_url(), id)

    def get_search_url(self, id, term):
        return "{0}/{1}/item?search={2}".format(self.get_url(), id, term)

    def find_by_list_id(self, list_id):
        response = self._execute("GET", "{0}/{1}/item".format(self.get_url(), list_id), None)

        results = []
        if response:
            results = self._get_response_objects(response)

        return results
        

    def save(self):
        payload = {
            "inventory-list-items": self.data.get("inventory-list-items")
        }

        response = self._execute("POST", self.get_save_url(self.data.get('id')), json.dumps(payload))
        obj = self._get_response_object(response)
        return obj


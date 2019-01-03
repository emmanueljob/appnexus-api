import json

from appnexusclient.models.base import Base

class InventoryListItem(Base):

    obj_name = "inventory-list"

    def set_domains(self, domains):
        if "inventory-list-items" not in self.data:
            self.data["inventory-list-items"] = []

        for domain in domains:
            row = {
                "url": domain,
                "include_children": False
            }
            self.data["inventory-list-items"].append(row)

    def set_apps(self, apps):
        if "inventory-list-items" not in self.data:
            self.data["inventory-list-items"] = []

        for app in apps:
            row = {
                "url": app,
                "include_children": False
            }
            self.data["inventory-list-items"].append(row)

    def get_save_url(self, id, advertiser_id=None):
        return "{0}/{1}/item".format(self.get_url(), id)

    def get_search_url(self, id, term):
        return "{0}/{1}/item?search={2}".format(self.get_url(), id, term)

    def save(self, data):
        payload = {
            self.data["inventory-list-items"]
        }

        response = self._execute("PUT", self.get_save_url(data.get('id')), json.dumps(payload))
        obj = self._get_response_object(response)
        return obj

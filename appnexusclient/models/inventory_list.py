from appnexusclient.models.base import Base


class InventoryList(Base):

    obj_name = "inventory-list"

    def find_by_name(self, name):
        response = self._execute("GET", self.get_search_url(name), None)

        results = []
        if response:
            results = self._get_response_objects(response)

        return results

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

    def get_save_url(self, obj_id, advertiser_id=None):
        return "{0}/{1}/item".format(self.get_url(), obj_id)

    def get_search_url(self, term):
        return "{0}?search={1}".format(self.get_url(), term)

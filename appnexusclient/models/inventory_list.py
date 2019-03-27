import json

from appnexusclient.models.base import Base


class InventoryList(Base):

    obj_name = "inventory-list"

    def find_by_name(self, name):
        response = self._execute("GET", self.get_search_url(name), None)

        results = []
        if response:
            results = self._get_response_objects(response)

        return results

    def find_by_id(self, id):
        response = self._execute("GET", "{0}?inventory_url_list_id={1}".format(self.get_url(), id), None)

        results = []
        if response:
            results = self._get_response_objects(response)

        return results

    def get_search_url(self, term):
        return "{0}?search={1}".format(self.get_url(), term)

    def delete(self):
        response = self._execute("DELETE", "{0}?id={1}".format(self.get_url(), self.data.get('id')), None)
        obj = json.loads(response.text)
        if obj.get('response').get('status') == "OK":
            pass
        else:
            print response.text
            print json.dumps(obj, indent=2)
            raise Exception("Bad response code")

        return True

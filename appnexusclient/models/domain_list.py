from appnexusclient.models.base import Base


class DomainList(Base):

    obj_name = "domain-list"

    def find_by_name(self, name):
        response = self._execute("GET", self.get_search_url(name), None)

        results = []
        if response:
            results = self._get_response_objects(response)

        return results

    def get_search_url(self, term):
        return "{0}?search={1}".format(self.get_url(), term)

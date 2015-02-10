from appnexusclient.models.base import Base


class PublisherBasedModel(Base):

    def find_one(self, id, publisher_id):
        self['publisher_id'] = publisher_id
        return self.find(id)

    def get_create_url(self):
        return "{0}?publisher_id={1}".format(self.get_url(), self.get('publisher_id'))

    def get_find_url(self, id):
        return "{0}?id={1}&publisher_id={2}".format(self.get_url(), id, self.get('publisher_id'))

    def find_by_publisher(self, publisher_id):
        url = "{0}?&publisher_id={1}".format(self.get_url(), publisher_id)

        response = self._execute("GET", url, None)

        results = []
        if response:
            results = self._get_response_objects(response)

        return results

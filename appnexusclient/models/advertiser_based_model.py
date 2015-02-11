from appnexusclient.models.base import Base


class AdvertiserBasedModel(Base):

    def find_one(self, id, advertiser_id):
        self['advertiser_id'] = advertiser_id
        return self.find(id)

    def get_create_url(self):
        return "{0}?advertiser_id={1}".format(self.get_url(), self.get('advertiser_id'))

    def get_find_url(self, id):
        return "{0}?id={1}&advertiser_id={2}".format(self.get_url(), id, self.get('advertiser_id'))

    def find_by_advertiser(self, advertiser_id, start_element=0, num_elements=100):
        url = "{0}?&advertiser_id={1}&start_element={2}&num_elements={3}".format(self.get_url(), advertiser_id, start_element, num_elements)

        response = self._execute("GET", url, None, start_element=start_element, num_elements=num_elements)

        results = []
        if response:
            results = self._get_response_objects(response)

        return results

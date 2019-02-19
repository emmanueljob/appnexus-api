from appnexusclient.models.advertiser_based_model import AdvertiserBasedModel


class LineItem(AdvertiserBasedModel):

    obj_name = "line-item"

    def find_by_advertiser(self, advertiser_id=None):
        if advertiser_id is None:
            return []
        else:
            url = "{0}?advertiser_id={1}".format(self.get_url(), advertiser_id)
            response = self._execute("GET", url, None)

            if response:
                return self._get_response_objects(response)
            else:
                return None

    def find_by_insertion_order(self, advertiser_id, insertion_order_id, start_element=0, num_elements=100):
        url = "{0}?advertiser_id={1}&insertion_order_id={2}".format(self.get_url(), advertiser_id, insertion_order_id)

        response = self._execute("GET", url, None, start_element=start_element, num_elements=num_elements)

        results = []
        if response:
            results = self._get_response_objects(response)

        return results

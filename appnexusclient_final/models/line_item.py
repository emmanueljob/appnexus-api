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

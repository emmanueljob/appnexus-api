import json

from appnexusclient.models.advertiser_based_model import AdvertiserBasedModel
from appnexusclient.models.profile import Profile
from appnexusclient.models.domain_list import DomainList


class Campaign(AdvertiserBasedModel):

    obj_name = "campaign"
    profile_obj = None

    def get_profile(self):
        self.profile_obj = json.loads(Profile(Campaign.connection).find_one(self.data.get('profile_id'), self.data.get('advertiser_id')))

        return self.profile_obj

    def find_by_line_item(self, advertiser_id, line_item_id, start_element=0, num_elements=100):
        url = "{0}?advertiser_id={1}&line_item_id={2}".format(self.get_url(), advertiser_id, line_item_id)

        response = self._execute("GET", url, None, start_element=start_element, num_elements=num_elements)

        results = []
        if response:
            results = self._get_response_objects(response)

        return results

imort json

from appnexusclient.models.advertiser_based_model import AdvertiserBasedModel


class Profile(AdvertiserBasedModel):

    obj_name = "profile"

    def set_deals(self, deals):
        deal_targets = []
        for deal in deals:
            deal_targets.append({'id': deal})

        self.data['deal_targets'] = deal_targets

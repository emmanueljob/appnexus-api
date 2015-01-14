from lib.models.advertiser_based_model import AdvertiserBasedModel
from lib.models.profile import Profile
from lib.models.domain_list import DomainList


class Campaign(AdvertiserBasedModel):

    obj_name = "campaign"
    profile_obj = None

    def set_domain_lists(self, domain_lists):
        profile = self.get_profile()
        domain_targets = []
        for domain_list in domain_lists:
            domain_targets.append(domain_list)
        profile['domain_list_targets'] = domain_targets
        profile.save()

    def get_domain_lists(self):
        profile = self.get_profile()
        list_ids = profile.get('domain_list_targets')

        loader = DomainList(Campaign.connection)
        rval = []
        for list_id in list_ids:
            rval.append(loader.find(list_id.get('id')))
        return rval

    def set_domains(self, domains):
        profile = self.get_profile()
        domain_targets = []
        for domain in domains:
            domain_targets.append({'domain': domain})
        profile['domain_targets'] = domain_targets
        profile.save()

    def get_domains(self):
        rval = []
        profile = self.get_profile()
        if profile.get('domain_targets'):
            for domain in profile.get('domain_targets'):
                rval.append(domain['domain'])
        return rval

    def set_deals(self, deals):
        profile = self.get_profile()
        deal_targets = []
        for deal in deals:
            deal_targets.append({'id': deal})
        profile['deal_targets'] = deal_targets
        profile.save()

    def get_deals(self):
        rval = []
        profile = self.get_profile()
        if profile.get('deal_targets'):
            for deal in profile.get('deal_targets'):
                rval.append(deal['id'])
        return rval

    def get_profile(self):
        if self.get('profile_id') > 0:
            if self.profile_obj is None:
                self.profile_obj = Profile(Campaign.connection).find_one(self.get('profile_id'), self.get('advertiser_id'))
        else:
            new_profile = Profile(Campaign.connection)
            new_profile['advertiser_id'] = self.get('advertiser_id')
            new_profile.create()
            self.profile_obj = new_profile
            self['profile_id'] = new_profile.get('id')

        return self.profile_obj

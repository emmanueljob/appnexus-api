from appnexusclient.models.advertiser_based_model import AdvertiserBasedModel
from appnexusclient.models.profile import Profile
from appnexusclient.models.domain_list import DomainList


class Campaign(AdvertiserBasedModel):

    obj_name = "campaign"
    profile_obj = None

    def set_domain_lists(self, domain_lists):
        profile = self.get_profile()
        domain_targets = []
        for domain_list in domain_lists:
            domain_targets.append(domain_list)
        profile['domain_list_targets'] = domain_targets
        profile['domain_list_action'] = "include"
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

    def set_member_targets(self, member_targets):
        profile = self.get_profile()
        target_objects = []
        for member_target in member_targets:
            target_objects.append({'id': member_target, 'action': 'include'})
        profile['member_targets'] = target_objects
        profile.save()

    def get_member_targets(self):
        rval = []
        profile = self.get_profile()
        if profile.get('member_targets'):
            for member_target in profile.get('member_targets'):
                rval.append(member_target['id'])
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

    def find_by_line_item(self, advertiser_id, line_item_id, start_element=0, num_elements=100):
        url = "{0}?advertiser_id={1}&line_item_id={2}".format(self.get_url(), advertiser_id, line_item_id)

        response = self._execute("GET", url, None, start_element=start_element, num_elements=num_elements)

        results = []
        if response:
            results = self._get_response_objects(response)

        return results

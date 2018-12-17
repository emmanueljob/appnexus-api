import json

from appnexusclient.models.advertiser_based_model import AdvertiserBasedModel


class Profile(AdvertiserBasedModel):

    obj_name = "profile"

    def set_domain_lists(self, domain_lists):
        domain_targets = []
        for domain_list in domain_lists:
            domain_targets.append(domain_list)

        self.data['domain_list_targets'] = domain_targets
        self.data['domain_list_action'] = "include"

    def get_domain_lists(self):
        list_ids = profile.get('domain_list_targets')

        loader = DomainList(Campaign.connection)
        rval = []
        for list_id in list_ids:
            rval.append(loader.find(list_id.get('id')))
        return rval

    def set_domains(self, domains):
        domain_targets = []
        for domain in domains:
            domain_targets.append({'domain': domain})

        self.data['domain_targets'] = domain_targets

    def get_domains(self):
        rval = []
        if self.data.get('domain_targets'):
            for domain in self.data.get('domain_targets'):
                rval.append(domain['domain'])

        return rval

    def set_member_targets(self, member_targets):
        target_objects = []
        for member_target in member_targets:
            target_objects.append({'id': member_target, 'action': 'include'})

        self.data['member_targets'] = target_objects

    def get_member_targets(self):
        rval = []
        if self.data.get('member_targets'):
            for member_target in self.data.get('member_targets'):
                rval.append(member_target['id'])

        return rval

    def set_placement_targets(self, placement_targets):
        target_objects = []
        for placement_target in placement_targets:
            target_objects.append({'id': placement_target})

        self.data['placement_targets'] = target_objects
        self.data['inventory_action'] = 'include'
        self.data['allow_unaudited'] = True

    def set_deals(self, deals):
        deal_targets = []
        for deal in deals:
            deal_targets.append({'id': deal})

        self.data['deal_targets'] = deal_targets

    def get_deals(self):
        rval = []
        if self.data.get('deal_targets'):
            for deal in self.data.get('deal_targets'):
                rval.append(deal['id'])

        return rval

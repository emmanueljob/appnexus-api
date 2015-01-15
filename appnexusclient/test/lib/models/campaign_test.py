import unittest
import json

from appnexusclient.lib.models.campaign import Campaign
from appnexusclient.lib.models.domain_list import DomainList
from appnexusclient.test.lib.base import Base


class CampaignTest(Base):

    def testCreate(self):
        campaign = Campaign(CampaignTest.conn)
        campaign['name'] = "Python Test"
        campaign['state'] = "inactive"
        campaign['advertiser_id'] = 136402
        campaign['line_item_id'] = 226154
        campaign['inventory_type'] = "direct"
        result = campaign.create()
        assert result == campaign.get('id')

    def testGet(self):
        loader = Campaign(CampaignTest.conn)
        campaigns = loader.find()
        for campaign in campaigns:
            assert campaign.get('name') is not None

    def testFlowNewCampaign(self):

        campaign = Campaign(CampaignTest.conn).find_one(470025, 136402)
        campaign.set_domains(["www.cnn.com"])
        campaign.save()

        reloaded_campaign = Campaign(CampaignTest.conn).find_one(470025, 136402)
        assert reloaded_campaign.get_domains() == ['cnn.com']

        reloaded_campaign.set_domains(['www.espn.com'])
        reloaded_campaign.save()

        reloaded_campaign = Campaign(CampaignTest.conn).find_one(470025, 136402)
        assert reloaded_campaign.get_domains() == ['espn.com']

        reloaded_campaign.set_deals([1999])
        reloaded_campaign.save()

        reloaded_campaign = Campaign(CampaignTest.conn).find_one(470025, 136402)
        assert reloaded_campaign.get_deals() == [1999]

        reloaded_campaign.set_deals([1999, 1998])
        reloaded_campaign.save()

        reloaded_campaign = Campaign(CampaignTest.conn).find_one(470025, 136402)
        assert sorted(reloaded_campaign.get_deals()) == sorted([1999, 1998])

    def testSetDomainList(self):

        campaign = Campaign(CampaignTest.conn).find_one(470025, 136402)
        domain_list = DomainList(CampaignTest.conn).find(6354)
        campaign.set_domain_lists([domain_list])
        campaign.save()

        reloaded_campaign = Campaign(CampaignTest.conn).find_one(470025, 136402)
        lists = reloaded_campaign.get_domain_lists()

        actual = []
        for domain in lists[0].get('domains'):
            actual.append(domain)

        assert sorted(['espn.com', 'cnn.com']) == sorted(actual)

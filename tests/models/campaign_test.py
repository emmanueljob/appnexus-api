import unittest
import json

from appnexusclient.models.campaign import Campaign
from appnexusclient.models.domain_list import DomainList
from tests.base import Base


class CampaignTest(Base):

    def testGet(self):
        loader = Campaign(CampaignTest.conn)
        campaigns = json.loads(loader.find())
        for campaign in campaigns.get('data').get('response').get('campaigns'):
            assert campaign.get('name') is not None

    def testFindByAdvertiser(self):
        adv_id = 482212
        loader = Campaign(CampaignTest.conn)
        campaigns = json.loads(loader.find_by_advertiser(adv_id))

        for campaign in campaigns.get('data').get('response').get('campaigns'):
            assert campaign.get('advertiser_id') == adv_id

    def testGetById(self):
        advertiser_id = 482212
        campaign_id = 7737907
        loader = Campaign(CampaignTest.conn)
        campaign = json.loads(loader.find_one(campaign_id, advertiser_id)).get('data').get('response').get('campaign')
        assert campaign_id == campaign.get('id')


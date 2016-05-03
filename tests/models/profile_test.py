import unittest
import json

from appnexusclient.models.profile import Profile
from tests.base import Base


class ProfileTest(Base):

    def testCreate(self):
        profile = Profile(ProfileTest.conn)
        profile['advertiser_id'] = 136402
        profile['deal_targets'] = [{'id': 1999}]
        profile['domain_targets'] = [{'domain': 'www.espn.com'}]
        result = profile.create()
        assert result == profile.get('id')

    def testGet(self):
        loader = Profile(ProfileTest.conn)
        profiles = loader.find()
        for profile in profiles:
            assert profile.get('id') is not None

    def testGetById(self):
        profile_id = 50161408
        advertiser_id = 454980
        loader = Profile(ProfileTest.conn)
        profile = loader.find_one(profile_id, advertiser_id)
        print profile
        assert profile_id == profile.get('id')

import unittest
import json
from appnexusclient.models.publisher_profile import PublisherProfile
from tests.base import Base

class TestPublisherProfile(Base):

    # test creation of profile
    def test_profile_create(self):
        profile = PublisherProfile(TestPublisherProfile.conn)
        result = profile.create_profile(169883, 1808327)
        print 'RESULT: ', result

    # def test_find(self):
    #     profile = PublisherProfile(TestPublisherProfile.conn)
    #     profiles = profile.find()
    #     for profile in profiles:
    #         if profile['publisher_id'] == 169883:
    #             print profile.get('id')
    #
    #     assert 1 == 1

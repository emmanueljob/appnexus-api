import unittest
import json

from appnexusclient.models.creative import Creative
from appnexusclient.models.template import Template
from tests.base import Base


class CreativeTest(Base):

    def testCreate(self):
        creative = Creative(CreativeTest.conn)
        creative['advertiser_id'] =  176051
        creative['name'] = 'Default Creative'
        creative['allow_ssl_audit'] = True
        creative['content'] = 'document.write(<test></test>);'
        creative['content_secure'] = 'document.write(<test></test>);'
        creative['original_content'] = '<test></test>'
        creative['original_content_secure'] = '<test></test>'
        creative['width'] = 120
        creative['height'] = 600
        creative['template'] = {'id': 6}
        result = creative.create()
        assert result == creative.get('id')

    def testUpdate(self):
        creative_id = 44122663
        loader = Creative(CreativeTest.conn)
        # creative_id, advertiser_id
        creative = loader.find_one(creative_id, 176051)
        creative['name'] = "updated matt/eman"
        creative['audit_status'] = "pending"
        creative['allow_audit'] = True
        creative.save()

    def testGet(self):
        loader = Creative(CreativeTest.conn)
        creatives = loader.find()
        for creative in creatives:
            assert creative.get('id') is not None

    def testGetById(self):
        creative_id = 44122663
        loader = Creative(CreativeTest.conn)
        creative = loader.find_one(creative_id, 176051)
        print(creative)
        assert creative_id == creative.get('id')

    def testGetOneTemplate(self):
        loader = Template(CreativeTest.conn)
        template = loader.find(1)
        print(template)

    def testGetTemplates(self):
        loader = Template(CreativeTest.conn)
        templates = loader.get_standard_only()
        for template in templates:
            print("$$$$$$$$$$$$$$$$$$$$$$$")
            print(template)
            print("$$$$$$$$$$$$$$$$$$$$$$$")
            assert template.get('id') is not None


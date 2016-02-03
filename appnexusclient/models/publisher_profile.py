from appnexusclient.models.publisher_based_model import PublisherBasedModel

class PublisherProfile(PublisherBasedModel):

    obj_name = "profile"

    def create_profile(self, publisher_id, placement_id):
        self['publisher_id'] = publisher_id
        self['placement_targets'] = [{'id': placement_id}]
        return self.create()

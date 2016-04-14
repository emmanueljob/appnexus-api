from appnexusclient.models.base import Base


class Template(Base):

    obj_name = "template"

    def get_standard_only(self):
		url = "{0}?member_id=null".format(self.get_url())
		response = self._execute("GET", url, None)

		if response:
			return self._get_response_objects(response)
		else:
			return None



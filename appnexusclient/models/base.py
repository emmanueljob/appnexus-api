import json
import requests

from ..service.connection import AuthException
from ..utility.appnexus_list import AppnexusList


class Base(dict):

    connection = None

    # Needs to be defined in the subclass
    obj_name = None

    def __init__(self, connection, data=None):
        self.data = data
        Base.connection = connection
        super(Base, self).__init__()

    def get_url(self):
        return "{0}/{1}".format(Base.connection.url, self.obj_name)

    def get_create_url(self):
        return self.get_url()

    def get_find_url(self, id):
        return "{0}?id={1}".format(self.get_url(), id)

    def get_save_url(self, obj_id, advertiser_id):
        return "{0}?id={1}&advertiser_id={2}".format(self.get_url(), obj_id, advertiser_id)

    def find(self, id=None, start_element=0, num_elements=100):
        if id is None:
            response = self._execute("GET", self.get_url(), None, start_element=start_element, num_elements=num_elements)

            rval = []
            if response:
                rval = self._get_response_objects(response)
            return rval
        else:
            response = self._execute("GET", self.get_find_url(id), None)

            if response:
                return self._get_response_object(response)
            else:
                return None

    def create(self):
        response = self._execute("POST", self.get_create_url(), json.dumps({self.obj_name: self.export_props()}))
        obj = self._get_response_object(response)
        return obj

    def delete(self):
        response = self._execute("DELETE", self.get_find_url(self.id), None)
        obj = json.loads(response.text)
        if obj.get('response').get('status') == "OK":
            pass
        else:
            raise Exception("Bad response code")

        return True

    def save(self, data):
        payload = {
            self.obj_name: data
        }

        response = self._execute("PUT", self.get_save_url(data.get('id'), data.get('advertiser_id')), json.dumps(payload))
        obj = self._get_response_object(response)
        return obj

    def _execute(self, method, url, payload, start_element=0, num_elements=100):
        result = None
        try:
            result = self._execute_no_reauth(method, url, payload, False, start_element, num_elements)
        except AuthException as e:
            # could be an expired auth token, reauth and try again
            Base.connection.authorize()
            result = self._execute_no_reauth(method, url, payload)

        return result

    def _execute_no_reauth(self, method, url, payload, skip_auth=False, start_element=0, num_elements=100):
        headers = {}
        if not skip_auth:
            headers = Base.connection.get_authorization()

        # add headers to help AppNexus debug.
        headers['x-session-data'] = json.dumps({"user_id": "146854", "user_type": "member", "entity_id": 1361})
        result = None

        if method == "GET":
            if start_element is not None:
                if '?' in url:
                    url = "{0}&start_element={1}&num_elements={2}".format(url, start_element, num_elements)
                else:
                    url = "{0}?start_element={1}&num_elements={2}".format(url, start_element, num_elements)
            print("curl -H 'Authorization: {0}' '{1}'".format(headers.get('Authorization', ''), url))
            result = requests.get(url, headers=headers)
        elif method == "POST":
            print("curl -XPOST -H 'Authorization: {0}' -d '{1}' '{2}'".format(headers.get('Authorization', ''), payload, url))
            result = requests.post(url, headers=headers, data=payload)
        elif method == "PUT":
            print("curl -XPUT -H 'Authorization: {0}' -d '{1}' '{2}'".format(headers.get('Authorization', ''), payload, url))
            result = requests.put(url, headers=headers, data=payload)
        elif method == "DELETE":
            print("curl -XDELETE -H 'Authorization: {0}' '{1}'".format(headers.get('Authorization', ''), url))
            result = requests.delete(url, headers=headers)
        else:
            raise Exception("Unknown method")

        # Unauthorized
        if result is None or result.status_code == 401:
            raise AuthException()

        return result

    def _get_response_objects(self, response):
        obj = json.loads(response.text)
        rval = {}
        rval["response_code"] = response.status_code
        if obj.get('response').get('status') == "OK":
            rval["msg_type"] = "success"
            rval["msg"] = ""
            rval["data"] = obj
            rval["request_body"] = ""
        else:
            rval["msg_type"] = "error"
            rval["msg"] = ""
            rval["data"] = obj

        return json.dumps(rval)

    def _get_response_object(self, response):
        obj = json.loads(response.text)
        rval = {}
        rval["response_code"] = response.status_code
        if obj.get('response').get('status') == "OK":
            rval["msg_type"] = "success"
            rval["msg"] = ""
            rval["data"] = obj
            rval["request_body"] = ""
        else:
            rval["msg_type"] = "error"
            rval["msg"] = ""
            rval["data"] = obj

        return json.dumps(rval)

    def import_props(self, props):
        for key, value in props.items():
            self[key] = value

    def export_props(self):
        rval = {}
        # do this an obvious way because using __dict__ gives us params we dont need.
        for key, value in self.items():
            rval[key] = value

        return rval

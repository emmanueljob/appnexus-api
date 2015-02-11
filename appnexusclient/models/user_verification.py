import base64
import calendar
import M2Crypto
import json
import requests
import time

from appnexusclient.models.base import Base


class UserVerification(Base):

    obj_name = "user-verification"

    def create_token(self):
        response = self._execute("POST", self.get_create_url(), None)

        obj = json.loads(response.text)
        if obj.get('response').get('status') == "OK":
            pass
        else:
            raise Exception("Bad response code")

        return obj.get('response').get('user-token')

    def get_token_url(self, id):
        return "{0}?user_token={1}".format(self.get_url(), id)

    def get_user_id(self, id):
        response = self._execute_no_reauth("GET", self.get_token_url(id), None, skip_auth=True, start_element=None)

        obj = json.loads(response.text)
        if obj.get('response').get('status') == "OK":
            pass
        else:
            # Bad User ID
            return -2

        return obj.get('response').get('user-id')

    def get_authorization(self, user_id, plugin_id, key):
        current_time = int(calendar.timegm(time.gmtime()))

        rsakey = M2Crypto.RSA.load_key_string(key)

        message = "{0}|{1}".format(str(current_time), str(user_id))
        encrypted = rsakey.private_encrypt(message, M2Crypto.RSA.pkcs1_padding)
        data = base64.b64encode(encrypted)

        payload = {'user_id': user_id, 'plugin_id': plugin_id, 'signature': data}
        url = '{0}/auth'.format(UserVerification.connection.url)
        response = requests.get(url, params=payload)

        obj = json.loads(response.text)
        if obj.get('response').get('status') == "OK":
            pass
        else:
            raise Exception("Bad response code " + response.text)

        return obj.get('response').get('token')

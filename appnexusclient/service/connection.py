import json
import os
import requests


class Connection:

    authorization_token = None
    tmp_file = None

    def __init__(self, username=None, password=None, url=None, tmp_file=None):
        Connection.password = password
        Connection.username = username
        Connection.url = url
        Connection.tmp_file = tmp_file

    def connect(self):
        headers = []
        headers.push(Connection.get_authorization())

    def set_auth_token(self, token):
        Connection.authorization_token = token
        self._save_auth_token()

    def get_authorization(self):
        if Connection.authorization_token is None:
            if Connection.tmp_file:
                # try using the auth token we have saved.
                if os.path.exists(Connection.tmp_file):
                    tmp_file = open(Connection.tmp_file, 'r+')
                    Connection.authorization_token = tmp_file.read()
            else:
                Connection.authorization_token = self.authorize()

        return {'Authorization': Connection.authorization_token}

    def authorize(self):
        auth_url = "{0}/auth".format(Connection.url)
        credentials = {
            "auth": {
                "username": Connection.username,
                "password": Connection.password
            }
        }

        try:
            response = requests.post(auth_url, data=json.dumps(credentials))
        except Exception as e:
            print "EXCEPTION"
            print e
            raise e

        if response is not None:
            obj = json.loads(response.text)
            if 'response' in obj and 'status' in obj.get('response') and obj.get('response').get('status') == "OK":
                Connection.authorization_token = obj.get('response').get('token')
            else:
                raise AuthException('unable to authenticate: ' + response.text)

        if Connection.tmp_file is not None:
            self._save_auth_token()

        return Connection.authorization_token

    def _save_auth_token(self):
        tmp_file = open(Connection.tmp_file, 'w')
        tmp_file.write(Connection.authorization_token)


class AuthException(Exception):
    pass

import requests
import json


class Connection:

    def __init__(self, username=None, password=None, url=None):
        Connection.password = password
        Connection.username = username
        Connection.url = url

    def connect(self):
        headers = []
        headers.push(Connection.get_authorization())

    def get_authorization(self):
        if Connection.authorization_token is None:
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

        response = requests.post(auth_url, data=json.dumps(credentials))

        if response is not None:
            obj = json.loads(response.text)
            if 'response' in obj and 'status' in obj.get('response') and obj.get('response').get('status') == "OK":
                Connection.authorization_token = obj.get('response').get('token')
            else:
                raise Exception('unable to authenticate')

        return Connection.authorization_token

import json
import requests


class Base(dict):

    connection = None

    # Needs to be defined in the subclass
    obj_name = None

    def __init__(self, connection):
        Base.connection = connection
        super(Base, self).__init__()

    def get_url(self):
        return "{0}/{1}".format(Base.connection.url, self.obj_name)

    def get_create_url(self):
        return self.get_url()

    def get_find_url(self, id):
        return "{0}?id={1}".format(self.get_url(), id)

    def find(self, id=None):
        if id is None:
            response = self._execute("GET", self.get_url(), None)

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
        if id in self:
            del self['id']

        response = self._execute("POST", self.get_create_url(), json.dumps({self.obj_name: self.export_props()}))
        obj = self._get_response_object(response)
        self.import_props(obj)

        return self.get('id')

    def delete(self):
        response = self._execute("POST", self.get_find_url(self.id), None)
        obj = json.loads(response.text)
        if obj.get('response').get('status') == "OK":
            pass
        else:
            raise Exception("Bad response code")

        return True

    def save(self):
        if self.get('id') is None or self.get('id') == 0:
            raise Exception("cant update an object with no id")

        response = self._execute("PUT", self.get_find_url(self.get('id')), json.dumps({self.obj_name: self.export_props()}))
        obj = self._get_response_object(response)
        self.import_props(obj)

        return self.get('id')

    def _execute(self, method, url, payload):

        headers = Base.connection.get_authorization()

        if method == "GET":
            return requests.get(url, headers=headers)
        elif method == "POST":
            print "curl -XPOST -H 'Authorization: {0}' -d '{1}' '{2}'".format(headers['Authorization'], payload, url)
            return requests.post(url, headers=headers, data=payload)
        elif method == "PUT":
            return requests.put(url, headers=headers, data=payload)
        elif method == "DELETE":
            return requests.delete(url, headers=headers)
        else:
            raise Exception("Unknown method")

    def _get_response_objects(self, response):
        rval = []
        obj = json.loads(response.text)
        if obj.get('response').get('status') == "OK":
            results = obj.get('response').get('{0}s'.format(self.obj_name))
            for result in results:
                new_obj = self.__class__(Base.connection)
                new_obj.import_props(result)
                rval.append(new_obj)
        else:
            raise Exception("Bad response code")

        return rval

    def _get_response_object(self, response):
        obj = json.loads(response.text)
        new_obj = None
        if obj.get('response').get('status') == "OK":
            result = obj.get('response').get(self.obj_name)
            new_obj = self.__class__(Base.connection)
            new_obj.import_props(result)
        else:
            print "RESULT:"
            print response.text
            raise Exception("Bad response code")

        return new_obj

    def import_props(self, props):
        for key, value in props.iteritems():
            self[key] = value

    def export_props(self):
        rval = {}
        # do this an obvious way because using __dict__ gives us params we dont need.
        for key, value in self.iteritems():
            rval[key] = value

        return rval

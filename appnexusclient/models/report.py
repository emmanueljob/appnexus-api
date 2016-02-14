import json
import requests

from appnexusclient.models.base import Base


class Report(Base):

    obj_name = "report"
    
    def run_report(self, params):
        pub_id = "720189"
        url = "{0}?publisher_id={1}".format(self.get_url(), pub_id)
        response = self._execute("POST", url, params)
        obj = json.loads(response.text)
        report_id = None
        if obj.get('response').get('status') == "OK":
            report_id = obj.get('response').get('report_id')
        else:
            raise Exception("Bad response code " + response.text)
        return report_id

    def ready(self):
        

    def get_download_url(self, id):
        url = "{0}?id={1}".format(self.get_url(), id)
        response = self._execute("GET", url, None)
        obj = json.loads(response.text)
        download_url = None
        if obj.get('response').get('status') == "OK":
            status = obj.get('response').get('execution_status')
            if status == "ready":
                download_url = obj.get('response').get('report').get('url')
        else:
            raise Exception("Bad response code " + response.text)
        return download_url
        
    def download(self, url, local_filename):
        url = "{0}/{1}".format(Report.connection.url, url)
        print url
        headers = Report.connection.get_authorization()
        r = requests.get(url, headers=headers, stream=True)
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024): 
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)

        return True

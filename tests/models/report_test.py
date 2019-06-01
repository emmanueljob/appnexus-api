import unittest
import json

from appnexusclient.models.report import Report
from tests.base import Base


class ReportTest(Base):

    def testRunReport(self):
        loader = Report(ReportTest.conn)
        params = """
{
    "report":
    {
        "report_type":"network_publisher_analytics",
        "columns":[
            "day",
            "buyer_member_id",
            "buyer_member_name",
            "line_item_name",
            "line_item_id",
            "placement_id",
            "creative_id",
            "deal_id",
            "deal_name",
            "imps_total",
            "imps_sold",
            "imps_default",
            "imps_blank",
            "external_impression",
            "external_click",
            "clicks",
            "total_convs"
        ],
        "row_per":[
            "day",
            "buyer_member_id",
            "line_item_id",
            "placement_id",
            "creative_id"
        ],
        "report_interval":"last_7_days",
        "format":"csv"
    }
}
        """

        report_id = loader.run_report(params)
        assert report_id != None
        print(report_id)

    def testGetDownloadUrl(self):
        loader = Report(ReportTest.conn)
        id = "4f283b5ed25d8aee2e4d0fc16597aef9"
        url = loader.get_download_url(id)
        assert url != None
        print(url)
        
    def testDownload(self):
        loader = Report(ReportTest.conn)
        url = "report-download?id=4f283b5ed25d8aee2e4d0fc16597aef9"
        result = loader.download(url, '/tmp/appnexus_test.csv')
        assert result == True
        

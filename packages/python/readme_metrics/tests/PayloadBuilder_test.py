import pytest
import requests
import json

from readme_metrics import MetricsApiConfig
from readme_metrics.PayloadBuilder import PayloadBuilder


# fetch json requests
class DataFetcher:
    def getJSON(self, url):
        res = requests.get(url)
        return res.json()

    def postJSON(self, url, param):
        res = requests.post(url, data=json.dumps(dict(param)))
        return res.json()

    def putJSON(self, url, param):
        res = requests.put(url, data=json.dumps(dict(param)))
        return res.json()


class TestPayloadBuilder:
    """
    Unit Tests for Payload Builder to make sure the created payloads are created
    correctly to the json request.

    Requests data can either be grabbed from an actual request, or maybe fake some JSON
    data that's similar in datatype as the one PayloadBuilder receives.

    Basic pattern is create payload, get data, compare, then assert.
    """

    def setUp(self):
        self.data_fetcher = DataFetcher()

    def createPayload(self, config):
        # use this to test different blacklist/whitelist/devmode/groupfunc
        # return the payload from the custom config
        return PayloadBuilder(
            config.BLACKLIST,
            config.WHITELIST,
            config.IS_DEVELOPMENT_MODE,
            config.GROUPING_FUNCTION,
        )

    def getMetricData(self):
        # function on getting the metric data
        res = None
        return res

    def compareRequests(self, fromReq, fromPayload):
        # Compare the two contents and check if they are similar(?)
        return True

    @pytest.mark.skip(reason="@todo")
    def testBlackListed(self, url):

        # Tests when the website is blacklisted
        # payload = createPayload(MetricsApiConfig(#params here))
        # jsonRes = self.data_fetcher.getJSON(url)
        # readMeRes = self.getMetricData()
        # similar = compareRequests(jsonRes, readMeRes)
        # self.assertTrue(similar)
        pass

    @pytest.mark.skip(reason="@todo")
    def testWhiteListed(self):
        # Tests when the website is whitelisted
        # payload = createPayload(MetricsApiConfig(#params here))
        # jsonRes = self.data_fetcher.getJSON(url)
        # readMeRes = self.getMetricData()
        # similar = compareRequests(jsonRes, readMeRes)
        # self.assertTrue(similar)
        pass

    @pytest.mark.skip(reason="@todo")
    def testProduction(self):
        # Tests when the website is called in production
        # payload = createPayload(MetricsApiConfig(#params here))
        # jsonRes = self.data_fetcher.getJSON(url)
        # readMeRes = self.getMetricData()
        # similar = compareRequests(jsonRes, readMeRes)
        # self.assertTrue(similar)
        pass

    @pytest.mark.skip(reason="@todo")
    def testDevelopment(self):
        # Tests when the website is called in development mode
        # payload = createPayload(MetricsApiConfig(#params here))
        # jsonRes = self.data_fetcher.getJSON(url)
        # readMeRes = self.getMetricData()
        # similar = compareRequests(jsonRes, readMeRes)
        # self.assertTrue(similar)
        pass

    # for test GET/POST/PUT I'm putting the status code tests for now since we cant
    # verify the body yet for status 401 and 403, they can also be moved to
    # blacklisted(?)
    @pytest.mark.skip(reason="@todo")
    def testGET(self):
        # payload = createPayload(MetricsApiConfig(#params here))

        # Test GET with 200
        # jsonRes = self.data_fetcher.getJSON(url)
        # readMeRes = self.getMetricData()
        # similar = compareRequests(jsonRes, readMeRes)
        # self.assertTrue(similar)

        # same pattern with these:
        # Test GET with 400 (Bad Request)
        # Test GET with 401 (Unauthorized)
        # Test GET with 403 (Forbidden)
        # Test GET with 404 (Not Found)
        pass

    @pytest.mark.skip(reason="@todo")
    def testPOST(self):
        # payload = createPayload(MetricsApiConfig(#params here))

        # Test POST with 200
        # jsonRes = self.data_fetcher.postJSON(url, param)
        # readMeRes = self.getMetricData()
        # similar = compareRequests(jsonRes, readMeRes)
        # self.assertTrue(similar)

        # same pattern with these:
        # Test POST with 400 (Bad Request)
        # Test POST with 401 (Unauthorized)
        # Test POST with 403 (Forbidden)
        # Test POST with 404 (Not Found)
        pass

    @pytest.mark.skip(reason="@todo")
    def testPUT(self):
        # payload = createPayload(MetricsApiConfig(#params here))

        # Test PUT with 200
        # jsonRes = self.data_fetcher.putJSON(url, param)
        # readMeRes = self.getMetricData()
        # similar = compareRequests(jsonRes, readMeRes)
        # self.assertTrue(similar)

        # same pattern with these:
        # Test PUT with 400 (Bad Request)
        # Test PUT with 401 (Unauthorized)
        # Test PUT with 403 (Forbidden)
        # Test PUT with 404 (Not Found)
        pass

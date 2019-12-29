import os
import sys
import json
import unittest
import requests
from unittest.mock import patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from mapsbr.helpers.request import get_geojson


class TestRequestWrapper(unittest.TestCase):

    @patch.object(requests.Session, "get")
    def test_request_if_raises_HTTP_error(self, mocked_get):
        mocked_get.side_effect = requests.exceptions.HTTPError
        with self.assertRaises(requests.exceptions.HTTPError):
            get_geojson("http://google.com")

    @patch("mapsbr.helpers.request.get_geojson")
    def test_request_if_raises_json_error(self, mocked_json):
        mocked_json.side_effect = json.JSONDecodeError
        with self.assertRaises(ValueError):
            get_geojson("http://google.com")


if __name__ == "__main__":
    unittest.main()

# vi: nowrap

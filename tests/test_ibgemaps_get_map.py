import os
import sys
import json
import unittest
import geopandas as gpd
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from mapsbr import ibgemaps


def mocked_get_geojson(url):
    json_path = Path(__file__).resolve().parent / "sample_jsons" / "3304_5"
    with json_path.open() as json_file:
        return json.load(json_file)


@patch("mapsbr.ibgemaps.get_geojson", mocked_get_geojson)
class TestGetMap(unittest.TestCase):

    def setUp(self):
        self.gdf = ibgemaps.get_map(3304, including="municipios")

    def test_get_map(self):
        self.assertTrue(isinstance(self.gdf, gpd.GeoSeries))


class TestGetMapMinusOne(unittest.TestCase):

    def setUp(self):
        self.test = ibgemaps.get_map(-1)

    def test_get_map(self):
        self.assertTrue(self.test.is_empty.values)


if __name__ == "__main__":
    unittest.main()

# vi: nowrap

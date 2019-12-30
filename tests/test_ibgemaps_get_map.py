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
class TestGetMapCode(unittest.TestCase):

    def setUp(self):
        self.gdf = ibgemaps.get_map(3304)

    def test_get_map(self):
        self.assertTrue(isinstance(self.gdf, gpd.GeoSeries))


@patch("mapsbr.ibgemaps.get_geojson", mocked_get_geojson)
class TestGetMapCalls(unittest.TestCase):

    @patch("mapsbr.helpers.ibgetools.ibge_encode")
    def test_get_map_with_geolevel(self, mocked_ibge_encode):
        mocked_ibge_encode.return_value = "Baixadas"
        ibgemaps.get_map("Baixadas", geolevel="mesoregions")
        mocked_ibge_encode.assert_called_with("Baixadas", "mesoregions")

    @patch("mapsbr.helpers.ibgetools.ibge_encode")
    def test_get_map_geolevel_none(self, mocked_ibge_encode):
        mocked_ibge_encode.return_value = "Baixadas"
        ibgemaps.get_map("Baixadas")
        mocked_ibge_encode.assert_called_with("Baixadas", "states")


class TestGetMapMinusOne(unittest.TestCase):

    def setUp(self):
        self.test = ibgemaps.get_map(-1)

    def test_get_map(self):
        self.assertTrue(self.test.is_empty.values)


if __name__ == "__main__":
    unittest.main()

# vi: nowrap

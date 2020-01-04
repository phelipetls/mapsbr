import os
import sys
import json
import unittest
import geopandas as gpd
from pathlib import Path
from unittest.mock import patch
from shapely.geometry import Point, Polygon, MultiPolygon, LineString

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from mapsbr import ibgemaps


def get_rj(*args, **kwargs):
    json_path = Path(__file__).resolve().parent / "sample_jsons" / "33"
    with json_path.open() as json_file:
        return json.load(json_file)


def get_rondonia(*args, **kwargs):
    json_path = Path(__file__).resolve().parent / "sample_jsons" / "11"
    with json_path.open() as json_file:
        return json.load(json_file)


geometries = (Point, Polygon, MultiPolygon, LineString)


@patch("mapsbr.ibgemaps.get_geojson", get_rj)
class TestGeoCodeWithCode(unittest.TestCase):

    def test_geocode_with_single_code(self):
        test = ibgemaps.geocode(33)
        self.assertIsInstance(test, geometries)

    def test_geocode_location_minus_one(self):
        test = ibgemaps.geocode(-1)
        self.assertTrue(test.is_empty)


@patch("mapsbr.ibgemaps.get_geojson", get_rj)
class TestGeoCodeWithName(unittest.TestCase):

    @patch("mapsbr.helpers.ibgetools.ibge_encode")
    def test_geocode_with_single_name(self, mocked_ibge_encode):
        # don't make a request, this is the code for rj
        mocked_ibge_encode.return_value = 33
        test = ibgemaps.geocode("Rio de Janeiro", geolevel="state")
        # test if ibge_encode is called right
        mocked_ibge_encode.assert_called_with("Rio de Janeiro", "state")
        # test if results are geometric objects
        self.assertIsInstance(test, geometries)

    def test_geocode_without_geolevel_raises(self):
        with self.assertRaises(AssertionError):
            ibgemaps.geocode("Rio de Janeiro")


geojsons = [get_rj(), get_rondonia()]


@patch("mapsbr.ibgemaps.get_geojson", side_effect=geojsons)
class TestGeoCodeWithList(unittest.TestCase):

    def test_geocode_with_various_codes(self, mocked_get_geojson):
        test = ibgemaps.geocode([33, 11])
        all_geometries = (isinstance(value, geometries) for value in test)
        self.assertTrue(all_geometries)

    def test_geocode_convert_to_geoseries(self, mocked_get_geojson):
        test = ibgemaps.geocode([33, 11])
        gdf = gpd.GeoSeries(test)
        self.assertIsInstance(gdf, gpd.GeoSeries)


if __name__ == "__main__":
    unittest.main(failfast=True)

# vi: nowrap

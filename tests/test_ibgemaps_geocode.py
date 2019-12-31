import os
import sys
import json
import unittest
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
        test = ibgemaps.geocode([33])
        # assert False, test
        cond = isinstance(test[0], geometries)
        self.assertTrue(cond and len(test) == 1)


@patch("mapsbr.ibgemaps.get_geojson", get_rj)
class TestGeoCodeWithName(unittest.TestCase):

    @patch("mapsbr.helpers.ibgetools.ibge_encode")
    def test_geocode_with_single_name(self, mocked_ibge_encode):
        # don't make a request, this is code for rj
        mocked_ibge_encode.return_value = 33
        test = ibgemaps.geocode(["Rio de Janeiro"])
        # test if ibge_encode is called right
        mocked_ibge_encode.assert_called_with("Rio de Janeiro", None)
        # test if results are geometric objects
        cond = isinstance(test[0], geometries)
        self.assertTrue(cond and len(test) == 1)


if __name__ == "__main__":
    unittest.main(failfast=True)

# vi: nowrap

import os
import sys
import json
import unittest
from pathlib import Path
from unittest.mock import patch
from shapely.geometry import Point, Polygon, MultiPolygon, LineString

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from mapsbr import ibgemaps


def get_json(filename=None):
    json_path = Path(__file__).resolve().parent / "sample_jsons" / filename
    with json_path.open() as json_file:
        return json.load(json_file)


rj, rondonia = get_json("33"), get_json("11")


class TestGeoCode(unittest.TestCase):

    geometries = (Point, Polygon, MultiPolygon, LineString)

    @patch("mapsbr.ibgemaps.get_geojson", side_effect=[rj] + [rj, rondonia] * 4)
    @patch("mapsbr.ibgemaps.ibgetools.ibge_encode", side_effect=[33, 11])
    def setUp(self, mock1, mock2):
        self.codes = ibgemaps.geocode([33, 11], "municipios")
        self.names = ibgemaps.geocode(["Rio de Janeiro", "Rondônia"], "municipios")

    def test_geocode_with_single_code(self):
        test = ibgemaps.geocode(33, "municipios")  # dummy call
        cond = all([isinstance(item, self.geometries) for item in test])
        self.assertTrue(cond)

    def test_geocode_with_codes(self):
        cond = all([isinstance(item, self.geometries) for item in self.codes])
        self.assertTrue(cond)

    def test_geocode_with_names(self):
        cond = all([isinstance(item, self.geometries) for item in self.names])
        self.assertTrue(cond)


if __name__ == "__main__":
    unittest.main()

# vi: nowrap

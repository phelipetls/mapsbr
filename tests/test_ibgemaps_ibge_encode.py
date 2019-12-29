import os
import sys
import json
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from mapsbr import tools


def mocked_get_geojson():
    json_path = Path(__file__).resolve().parent / "sample_json" / "estados"
    with json_path.open() as json_file:
        return json.load(json_file)


class TestUtils(unittest.TestCase):

    @patch("mapsbr.helpers.request.get_geojson", mocked_get_geojson)
    def test_geocode(self):
        locations = ["Rio de Janeiro", "Rondônia", "Acre"]
        test = tools.ibge_encode(locations)
        correct = [33, 11, 12]
        self.assertListEqual(test.tolist(), correct)

    @patch("mapsbr.helpers.request.get_geojson", mocked_get_geojson)
    def test_geocode_int(self):
        locations = ["Rio de Janeiro"]
        test = tools.ibge_encode(locations, "estado")
        correct = [33]
        self.assertListEqual(test.tolist(), correct)

    @patch("mapsbr.helpers.request.get_geojson", mocked_get_geojson)
    def test_geocode_optimization(self):
        tools.map_name_to_code = Mock()
        tools.ibge_encode(["Rio de Janeiro", "Rondônia", "Acre"])
        tools.map_name_to_code.assert_called_once_with("states")

    def test_geocode_if_raises_when_invalid_geo(self):
        with self.assertRaises(ValueError):
            tools.ibge_encode(["Rio de Janeiro"], "invalid")

    def test_geocode_if_raises_when_invalid_location_name_str(self):
        with self.assertRaises(AssertionError):
            tools.ibge_encode(["0", "1"])

    def test_geocode_if_raises_when_invalid_location_name_int(self):
        with self.assertRaises(AssertionError):
            tools.ibge_encode([0, 1])


if __name__ == "__main__":
    unittest.main()

# vi: nowrap

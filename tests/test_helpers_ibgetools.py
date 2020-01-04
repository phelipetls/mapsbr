import os
import sys
import json
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from mapsbr.helpers import ibgetools


def mocked_get_geojson(url):
    json_path = Path(__file__).resolve().parent / "sample_jsons" / "estados"
    with json_path.open() as json_file:
        return json.load(json_file)


@patch("mapsbr.helpers.ibgetools.get_geojson", mocked_get_geojson)
class TestIbgeEncode(unittest.TestCase):

    def test_ibge_encode(self):
        test = ibgetools.ibge_encode(["Rio de Janeiro", "Rondônia", "Acre"], "state")
        correct = [33, 11, 12]
        self.assertListEqual(test.tolist(), correct)

    def test_ibge_encode_int(self):
        test = ibgetools.ibge_encode("Rio de Janeiro", "state")
        correct = 33
        self.assertEqual(test, correct)

    def test_ibge_encode_if_raises_when_invalid_location_name_str(self):
        with self.assertRaises(AssertionError):
            ibgetools.ibge_encode(["0", "1"], "state")

    def test_ibge_encode_if_raises_when_invalid_location_name_int(self):
        with self.assertRaises(AssertionError):
            ibgetools.ibge_encode([0, 1], "state")


@patch("mapsbr.helpers.ibgetools.get_geojson", mocked_get_geojson)
class TestIbgeDecode(unittest.TestCase):

    def test_ibge_decode(self):
        locations = [33, 11, 12]
        test = ibgetools.ibge_decode(locations, "state")
        correct = ["Rio de Janeiro", "Rondônia", "Acre"]
        self.assertListEqual(test.tolist(), correct)

    def test_ibge_decode_int(self):
        locations = 33
        test = ibgetools.ibge_decode(locations, "state")
        correct = "Rio de Janeiro"
        self.assertEqual(test, correct)

    def test_ibge_decode_if_raises_when_invalid_location_name_int(self):
        with self.assertRaises(AssertionError):
            ibgetools.ibge_decode(["Rio de Janeiro"], "state")


if __name__ == "__main__":
    unittest.main(failfast=True)

# vi: nowrap

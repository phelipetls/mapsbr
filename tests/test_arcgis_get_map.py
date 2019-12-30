import os
import sys
import json
import unittest
from unittest.mock import patch
from pathlib import Path

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from mapsbr import arcgis


def get_downloaded_feature(n):
    jsonpath = Path(__file__).resolve().parent / "sample_jsons" / f"arcgis_{n}"
    with jsonpath.open() as jsonfile:
        return json.load(jsonfile)


all_jsons = [get_downloaded_feature(n) for n in range(1, 4)]


class TestArcGIS_GetMap(unittest.TestCase):

    @patch("mapsbr.arcgis.get_geojson", side_effect=all_jsons)
    def setUp(self, mocked_get_geojson):
        self.df = arcgis.get_map("GEOLOGIA")

    def test_if_df_is_not_empty(self):
        self.assertFalse(self.df.empty)

    def test_if_df_has_two_columns(self):
        self.assertTrue(len(self.df.columns) == 2)


def get_downloaded_search_result(n):
    jsonpath = Path(__file__).resolve().parent / "sample_jsons" / "services"
    with jsonpath.open() as jsonfile:
        return json.load(jsonfile)


class TestArcGIS_Search(unittest.TestCase):

    @patch("mapsbr.arcgis.get_geojson", get_downloaded_search_result)
    def setUp(self):
        self.search_results = arcgis.search()

    def test_if_search_results_are_not_none(self):
        self.assertFalse(self.search_results.empty)


if __name__ == "__main__":
    unittest.main()

# vi: nowrap

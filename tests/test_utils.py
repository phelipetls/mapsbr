import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from mapsbr.helpers import utils


class TestUtils(unittest.TestCase):

    def test_vectorized_get_str(self):
        D = {"A": 1, "B": 2, "C": 3, "D": 4}
        L = "A"
        test = utils.vectorized_get(D, L)
        correct = [1]
        self.assertListEqual([test], correct)

    def test_vectorized_get_list(self):
        D = {"A": 1, "B": 2, "C": 3, "D": 4}
        L = ["A", "B", "E"]
        test = utils.vectorized_get(D, L)
        correct = [1, 2, 0]
        self.assertListEqual(test.tolist(), correct)

    def test_get_features(self):
        D = {"invalid": "geojson"}
        with self.assertRaises(KeyError):
            utils.get_features(D)


if __name__ == "__main__":
    unittest.main()

# vi: nowrap

import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from mapsbr import ibgemaps


class TestUrlBuilders(unittest.TestCase):

    def test_build_url(self):
        test = "http://servicodados.ibge.gov.br/api/v2/malhas/3304?resolucao=0&formato=application/vnd.geo+json"
        correct = ibgemaps.build_url(3304)
        self.assertEqual(test, correct)

    def test_build_url_with_resolution(self):
        test = "http://servicodados.ibge.gov.br/api/v2/malhas/3304?resolucao=5&formato=application/vnd.geo+json"
        correct = ibgemaps.build_url(3304, including="municipalities")
        self.assertEqual(test, correct)


if __name__ == "__main__":
    unittest.main()

# vi: nowrap

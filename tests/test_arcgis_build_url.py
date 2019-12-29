import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from mapsbr import arcgis


class TestArcGIS(unittest.TestCase):

    def test_build_url(self):
        correct = "https://mapasinterativos.ibge.gov.br/arcgis/rest/services/BIOMA/MapServer/0/query?where=objectId>=0+and+objectId<1000&f=geojson"
        test = arcgis.build_url("BIOMA")
        self.assertEqual(test, correct)

    def test_build_url_different_baseurl(self):
        correct = "https://pgeo3.rio.rj.gov.br/arcgis/rest/services/Basicos/mapa_basico_UTM/MapServer/0/query?where=objectId>=0+and+objectId<1000&f=geojson"
        test = arcgis.build_url("Basicos/mapa_basico_UTM", baseurl="https://pgeo3.rio.rj.gov.br/arcgis/rest/services")
        self.assertEqual(test, correct)


if __name__ == "__main__":
    unittest.main()

# vi: nowrap

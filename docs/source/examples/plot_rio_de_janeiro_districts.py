"""
Rio de Janeiro (city) districts
===============================
"""

###############################################################################
# This example will explore the case of getting data from another
# ArcGIS server.
#
# We will use a `server <https://pgeo3.rio.rj.gov.br/arcgis/rest/services/>`__ that
# provides data on the city of Rio de Janeiro. Let's, for example, plot the district
# divisions.

from mapsbr import arcgis

districts = arcgis.get_map(
    service="Basicos/mapa_basico_UTM",
    layer=15,
    baseurl="https://pgeo3.rio.rj.gov.br/arcgis/rest/services/",
)

import matplotlib.pyplot as plt

districts.plot(color="w", edgecolor="steelblue")
plt.title("Rio de Janeiro city districts")
plt.gca().axis("off")

###############################################################################
# .. note:
#
#    This function unfortunately is considerably unreliable and only tested
#    in these two hosts. I'll surely put some work on improving it.
#
# From the same service, you could also plot some interesting things like
# the geographical distribution of municipal hospitals.

rj_districts = districts.plot(color="w", edgecolor="steelblue")

arcgis.get_map(
    service="Basicos/mapa_basico_UTM",
    layer=7,
    baseurl="https://pgeo3.rio.rj.gov.br/arcgis/rest/services/",
).plot(ax=rj_districts, color="black", marker="x", markersize=10)

plt.gca().axis("off")
plt.title("Municipal hospitals in Rio de Janeiro")

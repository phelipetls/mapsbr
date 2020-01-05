"""
Favelas in Rio de Janeiro
=========================
"""

###############################################################################
# This is another example in which we use data from the
# ArcGIS server of Rio de Janeiro city.
#
# This time, we'll try to visualize the distribution of slums or favelas
# in the city.
#
# Let's first try to get the map of the city and afterwards plot the favelas
# geometries.

import pandas as pd

pd.set_option("max_rows", 10)

from mapsbr import arcgis

districts = arcgis.get_map(
    service="Basicos/mapa_basico_UTM",
    layer=15,
    baseurl="https://pgeo3.rio.rj.gov.br/arcgis/rest/services/",
)

favelas = arcgis.get_map(
    service="SMH/Limites_de_Favelas",
    layer=0,
    baseurl="https://pgeo3.rio.rj.gov.br/arcgis/rest/services/",
)

###############################################################################
# Now, just to see what other interesting things we can do with GeoPandas
# and the Shapely library in general: let's calculate the geometries' areas.
#
# This will give us a rough idea about which favela is the biggest:

favelas["area"] = favelas.geometry.area
favelas = favelas.sort_values("area", ascending=False)

###############################################################################
# Now, here is what I wanna do: highlight the five biggest ones.
#
# This will be straight-forward to do with annotate method of matplotlib.

favelas["point"] = favelas.geometry.centroid  # calculate the geometry centroid

import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 7), constrained_layout=True)
districts.plot(color="white", edgecolor="slategray", ax=ax)
favelas.plot(color="orange", ax=ax)
favelas.query("Nome in @favelas.Nome.head()").plot(color="gray", ax=ax)

ax.axis("off")
ax.set_title("Favelas in Rio\nBiggest 5 highlighted")

for _, row in favelas.head().iterrows():
    ax.annotate(
        row.Nome,
        xy=(row.point.x, row.point.y),
        xytext=(5, 10),
        textcoords="offset points",
        arrowprops=dict(arrowstyle="->", color="black", connectionstyle="angle3"),
        bbox=dict(boxstyle="round", alpha=0.7, facecolor="silver"),
        color="k",
    )

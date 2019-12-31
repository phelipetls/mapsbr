"""
Choropleth map: brazil population by macroregion
================================================
"""

###############################################################################
#
# In this example we want to visualize brazilian population
# by macroregion.
#
# Let's first retrieve the data with the `seriesbr <seriesbr.readthedocs.io>`_ package.
from seriesbr import ibge

population = ibge.get_series(6462, 606, macroregions=True, last_n=1)

population

###############################################################################
# Then let's convert this `DataFrame` into a `GeoDataFrame` and assign
# to a column named "geometry" the macroregions' geometric objects.
#
# You can get a geometric object for a given location with the function 
# :py:func:`mapsbr.ibgemaps.geocode`. It can either be a location code or name. If
# it's a name, you'll need to pass its geographic level as the argument `geolevel` so
# it can properly get converted to a code.
#
# For example, `ibgemaps.geocode("Rio de Janeiro", geolevel="state")` if you want Rio
# de Janeiro state map or `ibgemaps.geocode("Rio de Janeiro", geolevel="municipality") if
# the map for Rio de Janeiro city.
#
# Notice that the column with the geometric objects *has* to be named geometry. Otherwise
# you'll need to call the `set_geometry("new_column")` method on the `GeoDataFrame`.

import geopandas as gpd
from mapsbr import ibgemaps

gdf = gpd.GeoDataFrame(population)
gdf["geometry"] = ibgemaps.geocode(population["Grande Região"], geolevel="macroregion")
gdf.plot(column="Valor", legend=True, edgecolor="w")

import matplotlib.pyplot as plt
plt.show()
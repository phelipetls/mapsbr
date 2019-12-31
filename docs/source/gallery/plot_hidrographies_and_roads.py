"""
Highways, railways and hidrographies
====================================
"""

###############################################################################
# Let's imagine you for some reason have to plot all brazilian hidrographies or
# highways. You can do this with the help of :py:mod:`mapsbr.arcgis` module.
#
# First let me explain how the ArcGIS API works. To get a map from somewhere
# you will first need a host (a server) from which you will retrieve the data.
# By default, this will be https://mapasinterativos.ibge.gov.br/arcgis/rest/.
#
# Each host stores its data in folders or services. You will need to search
# where exactly is the desired geometry.
#
# There is a function to help with that, but it is more featureful
# to do it in the browser, probably.

from mapsbr import arcgis, ibgemaps

arcgis.search()  # by default, it will search in services

###############################################################################
#

arcgis.search(where="folders")

###############################################################################
# For example, in our case, the geometries for highways, railways
# and hidrographies is in the service folder called BASEMAP.
#
# Inside the folder there are various layers, and we will also need those.
#
# The layer number for railway is 2, for highways is 3 and for hidrographies
# is 4.
#
# The function :py:func:`mapsbr.arcgis.get_map` takes arguments for all these
# things. But by default, it will search in an IBGE host, so you just need to pass
# the service and layer identifiers.

railways = arcgis.get_map("BASEMAP", layer=2)
highways = arcgis.get_map("BASEMAP", layer=3)
hidrographies = arcgis.get_map("BASEMAP", layer=4)

transports = railways, highways, hidrographies
titles = ["Railways", "Highways", "Hidrographies"]

###############################################################################
# Once we have it, let's now plot it.

import matplotlib.pyplot as plt

fig, axes = plt.subplots(nrows=1, ncols=3)
br = ibgemaps.get_map("BR")
for ax, transport, title in zip(axes.flat, transports, titles):
    br.plot(ax=ax, color="white", edgecolor="gray")
    transport.plot(ax=ax, column=transport.columns[1])
    ax.set_title(title)
    ax.axis("off")

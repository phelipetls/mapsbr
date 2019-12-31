.. mapsbr documentation master file, created by
   sphinx-quickstart on Mon Dec 30 18:28:27 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

MapsBR
======

.. toctree::
   :maxdepth: 2
   :caption: Contents:

**mapsbr** is a Python package to help you get brazilian geospatial data
from official sources like IBGE or ArcGIS API.

First it downloads a GeoJSON from the web with `requests <https://2.python-requests.org/en/master/>`__, which gets
parsed by `shapely <https://shapely.readthedocs.io/en/latest/manual.html#predicates-and-relationships>`__
and passed into a `geopandas <http://geopandas.org/>`__ structure, a ``GeoSeries`` or a ``GeoDataFrame``, which is a typical
``DataFrame`` with magic properties and methods concerning ``shapely`` geometric objects on top of it.

It's then, for example, trivial to plot a map or to make a `choropleth map <https://en.wikipedia.org/wiki/Choropleth_map>`__ with
``geopandas``. It does it very well with the help of `descartes <https://pypi.org/project/descartes/>`__ and
`matplotlib <https://matplotlib.org/>`__. But you can do many other things like calculate area, get the interesection of two geometries etc.

This package is inspired by the R package `geobr <https://github.com/ipeaGIT/geobr>`__.

Main Features
-------------

-  Get and plot maps from IBGE.
-  Get and plot maps from an ArcGIS source.

Examples
--------

Learn how to use the package in examples section:

.. toctree:: 

   gallery/index.rst

Quick Demo
----------

As a quick demonstration, let me demonstrate how one would plot the brazilian
map including many sub geographical levels:

.. ipython:: python

   from mapsbr import ibgemaps
   from matplotlib import pyplot as plt

   fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(10, 8), clear=True)

   geographic_levels = ["macroregions", "states", "mesoregions", "microregions", "municipalities"]

   for level, ax in zip(geographic_levels, axes.flat):
       ax.axis("off")
       ax.set_title("Brazil map with\n{}".format(level))
       ibgemaps.get_map("BR", including=level).plot(color="#bfd1d4", edgecolor="#ee9c1f", ax=ax)

   for ax in axes.flat:
       if not ax.has_data():
           fig.delaxes(ax)

   @savefig brazilian_maps.png
   fig.tight_layout()

License
-------

`MIT <https://github.com/phelipetls/mapsbr/blob/master/LICENSE>`__

Contributing
------------

Please feel free to open an issue or a pull request in case you find any
bugs or if you want to contribute. Thanks.

Support
-------

If you like the package, give this repo a star!

.. |brazilian_maps| image:: ../../figs/brazilian_maps.png


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

Installation
============

To install the latest version, run

.. code::

   $ pip3 install --upgrade mapsbr

Dependencies
------------

- `shapely <https://shapely.readthedocs.io/en/latest/>`__
- `geopandas <https://geopandas.readthedocs.io/en/latest/>`__
- `requests <https://2.python-requests.org/en/master/>`__
- `matplotlib <https://matplotlib.org>`__
- `descartes <https://pypi.org/project/descartes/>`__

Most of these python packages depend on another C++ library called geos, so you'll
need to install this. `Here's their GitHub repo <https://github.com/libgeos/geos>`__.

In short, if you're running Ubuntu, for example, you can install their development
libraries with the following command

.. code::

   $ sudo apt install libgeos++-dev libgeos-dev


Troubleshooting
---------------

If using the library cause a segmentation fault, it is likely because of some conflict
regarding the installation of libgeos.

What solved it for me was to uninstall shapely and the reinstall it with

.. code::

   $ pip3 install --no-binary shapely shapely

Check out `this issue <https://github.com/Toblerity/Shapely/issues/651>`__ for details.

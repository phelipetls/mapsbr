Tutorial
========

Let's learn the basics on how to use each module.

ibgemaps
--------

Maybe the most useful function here is :py:func:`mapsbr.ibgemaps.get_map`. It
lets you get geometric objects associated with a geographic space.

For example, if you want a map of Brazil including states, you'd
call:

.. ipython:: python

   from mapsbr import ibgemaps

   @savefig br_with_states.png
   ibgemaps.get_map("BR", including="states").plot()


Or, supposing you want the Amazonas state map with municipalities, you would call:

.. ipython:: python

   @savefig amazonas_with_municipalities.png
   ibgemaps.get_map("Amazonas", including="municipalities", geolevel="state").plot()

Notice that you need to specify if it is a state, a municipality, etc. This
avoid ambiguity, e.g., "Rio de Janeiro" is both a state and a municipality.

Another useful function is :py:func:`mapsbr.ibgemaps.geocode`, which is a more
specialized function to convert locations names into geometric objects (it doesn't
return a GeoSeries like :py:func:`mapsbr.ibgemaps.get_map`).

.. ipython:: python
   
   ibgemaps.geocode("Rio de Janeiro", geolevel="state")

It's useful when you want to convert a column with location names into a
geometric column:

.. ipython:: python

   import geopandas as gpd

   states = ["Rio de Janeiro", "Minas Gerais", "São Paulo", "Espírito Santo"]
   gdf = gpd.GeoDataFrame({"states": states})
   
   gdf

   gdf["geometry"] = ibgemaps.geocode(gdf.states, geolevel="state")

   gdf

arcgis
------

This module provides a general API to retrieve data from an ArcGIS server, as
some brazilian government institutions stores some interesting data in them,
e.g. IBGE.

As you want geospatial data, you'll most likely be looking for a MapServer type
of service in the ArcGIS server. They may be in the "Services Directory" on in
a subfolder within it.

To help you browse the available options you can use the functions
:py:func:`mapsbr.arcgis.folders` or :py:func:`mapsbr.arcgis.services`, which
will list all folders and services in a server, respectively.

As it shall be illustrated next, by default it will search in a `IBGE server
<https://mapasinterativos.ibge.gov.br/arcgis/rest/services/>`__.

.. ipython:: python

   from mapsbr import arcgis
   
   arcgis.folders()

   arcgis.services().head()

Now, imagine you're interested in the FAUNA service. You can take a look at the
available feature layers like this:

.. ipython:: python

   arcgis.layers("FAUNA")


Now, to get an actual layer, call :py:func:`mapsbr.arcgis.get_map`:

.. ipython:: python

   @savefig bioma.png
   arcgis.get_map("BIOMA", layer=0).plot(column="NOME", legend=True)

If you want to get a feature layer from another ArcGIS server, you will
need to specify its URL. For example:

.. ipython:: python

   @savefig rj.png
   arcgis.get_map(
       service="Basicos/mapa_basico_UTM",
       layer=15,
       baseurl="https://pgeo3.rio.rj.gov.br/arcgis/rest/services/",
   ).plot()

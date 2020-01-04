Introduction
============

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

Notice that you need to specify if it is a state, a municipality, etc., the
location geographic level. This avoid unambiguity, e.g., "Rio de Janeiro" is
both a state and a municipality.

Another useful function is :py:func:`mapsbr.ibgemaps.geocode`, which is a more
specialized function to convert locations names into geometric objects (it doesn't
return a GeoSeries like :py:func:`mapsbr.ibgemaps.get_map`).

.. ipython:: python
   
   ibgemaps.geocode("Rio de Janeiro", geolevel="state")

It's useful when you want to convert a location names column into a geometry column:

.. ipython:: python

   import geopandas as gpd

   states = ["Rio de Janeiro", "Minas Gerais", "São Paulo", "Espírito Santo"]
   gdf = gpd.GeoDataFrame({"states": states})

   gdf["geometry"] = ibgemaps.geocode(gdf.states, geolevel="state")

   gdf

arcgis
------



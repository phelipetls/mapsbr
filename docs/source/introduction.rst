Introduction
============

Let's learn the basics on how to use each module.

ibgemaps
--------

The function :py:func:`mapsbr.ibgemaps.get_map` gives you a GeoSeries with a
bunch of geometric objects depending on what you pass into it.

For example, if you want a map of the whole country including states, you'd
call:

.. ipython:: python

   from mapsbr import ibgemaps

   @savefig br_with_states.png
   ibgemaps.get_map("BR", including="states").plot()


But, suppose if you want the Amazonas state map including municipalities. You
would then actually need to know the Amazonas's IBGE code, but in fact you can
just pass the state name and specify its geographic level.

.. ipython:: python

   @savefig amazonas_with_municipalities.png
   ibgemaps.get_map("Amazonas", including="municipalities", geolevel="state").plot()

Another very useful function is :py:func`mapsbr.ibgemaps.geocode` which gives
you the geometric object associated with the passed value. If it doesn't find
any, it returns an empty geometry.

.. ipython:: python
   
   ibgemaps.geocode(["Rio de Janeiro"], geolevel="state")

This is most useful when you want the geometric objects of DataFrame column, for example.
You would then just call.

.. ipython:: python

   import geopandas as gpd

   states = ["Rio de Janeiro", "Minas Gerais", "São Paulo", "Espírito Santo"]
   gpd.GeoDataFrame({"states": states, "geometry": ibgemaps.geocode(states, geolevel="state")})

arcgis
------

This module is less high level

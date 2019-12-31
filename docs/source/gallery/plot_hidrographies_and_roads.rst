.. note::
    :class: sphx-glr-download-link-note

    Click :ref:`here <sphx_glr_download_gallery_plot_hidrographies_and_roads.py>` to download the full example code
.. rst-class:: sphx-glr-example-title

.. _sphx_glr_gallery_plot_hidrographies_and_roads.py:


Highways, railways and hidrographies
====================================

Let's imagine you for some reason have to plot all brazilian hidrographies or
highways. You can do this with the help of :py:mod:`mapsbr.arcgis` module.

First let me explain how the ArcGIS API works. To get a map from somewhere
you will first need a host (a server) from which you will retrieve the data.
By default, this will be https://mapasinterativos.ibge.gov.br/arcgis/rest/.

Each host stores its data in folders or services. You will need to search
where exactly is the desired geometry.

There is a function to help with that, but it is more featureful
to do it in the browser, probably.


.. code-block:: default


    from mapsbr import arcgis, ibgemaps

    arcgis.search()  # by default, it will search in services






.. only:: builder_html

    .. raw:: html

        <div>
        <style scoped>
            .dataframe tbody tr th:only-of-type {
                vertical-align: middle;
            }

            .dataframe tbody tr th {
                vertical-align: top;
            }

            .dataframe thead th {
                text-align: right;
            }
        </style>
        <table border="1" class="dataframe">
          <thead>
            <tr style="text-align: right;">
              <th></th>
              <th>name</th>
              <th>type</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <th>0</th>
              <td>AGRICOLA</td>
              <td>MapServer</td>
            </tr>
            <tr>
              <th>1</th>
              <td>atlas_mun</td>
              <td>MapServer</td>
            </tr>
            <tr>
              <th>2</th>
              <td>atlas_uf</td>
              <td>MapServer</td>
            </tr>
            <tr>
              <th>3</th>
              <td>BASEMAP</td>
              <td>MapServer</td>
            </tr>
            <tr>
              <th>4</th>
              <td>BIOMA</td>
              <td>MapServer</td>
            </tr>
            <tr>
              <th>5</th>
              <td>CLIMAS</td>
              <td>MapServer</td>
            </tr>
            <tr>
              <th>6</th>
              <td>compara_munAGRO</td>
              <td>MapServer</td>
            </tr>
            <tr>
              <th>7</th>
              <td>densidade_v2</td>
              <td>MapServer</td>
            </tr>
            <tr>
              <th>8</th>
              <td>domicilio_v2</td>
              <td>MapServer</td>
            </tr>
            <tr>
              <th>9</th>
              <td>DPA2010</td>
              <td>MapServer</td>
            </tr>
            <tr>
              <th>10</th>
              <td>entorno_v2</td>
              <td>MapServer</td>
            </tr>
            <tr>
              <th>11</th>
              <td>ExportWebMap</td>
              <td>GPServer</td>
            </tr>
            <tr>
              <th>12</th>
              <td>FAUNA</td>
              <td>MapServer</td>
            </tr>
            <tr>
              <th>13</th>
              <td>genero_V2</td>
              <td>MapServer</td>
            </tr>
            <tr>
              <th>14</th>
              <td>GEOLOGIA</td>
              <td>MapServer</td>
            </tr>
            <tr>
              <th>15</th>
              <td>grade_raster100</td>
              <td>MapServer</td>
            </tr>
            <tr>
              <th>16</th>
              <td>grade_raster10</td>
              <td>MapServer</td>
            </tr>
            <tr>
              <th>17</th>
              <td>grade_raster1</td>
              <td>MapServer</td>
            </tr>
            <tr>
              <th>18</th>
              <td>grade_raster500v2</td>
              <td>MapServer</td>
            </tr>
            <tr>
              <th>19</th>
              <td>grade_raster50</td>
              <td>MapServer</td>
            </tr>
            <tr>
              <th>20</th>
              <td>grade_raster5</td>
              <td>MapServer</td>
            </tr>
            <tr>
              <th>21</th>
              <td>grade_raster_estatistica</td>
              <td>MapServer</td>
            </tr>
            <tr>
              <th>22</th>
              <td>GRADE_VETOR</td>
              <td>MapServer</td>
            </tr>
            <tr>
              <th>23</th>
              <td>LOCALIDADES_CENSO2010</td>
              <td>MapServer</td>
            </tr>
            <tr>
              <th>24</th>
              <td>Mudancas_uso</td>
              <td>MapServer</td>
            </tr>
            <tr>
              <th>25</th>
              <td>recorte1_pop</td>
              <td>MapServer</td>
            </tr>
            <tr>
              <th>26</th>
              <td>recorte_pop_v1C</td>
              <td>MapServer</td>
            </tr>
            <tr>
              <th>27</th>
              <td>recorte_pop_v2C</td>
              <td>MapServer</td>
            </tr>
            <tr>
              <th>28</th>
              <td>recorte_pop_v3c</td>
              <td>MapServer</td>
            </tr>
            <tr>
              <th>29</th>
              <td>RECORTES</td>
              <td>MapServer</td>
            </tr>
            <tr>
              <th>30</th>
              <td>RELEVO</td>
              <td>MapServer</td>
            </tr>
            <tr>
              <th>31</th>
              <td>saneamento_v2</td>
              <td>MapServer</td>
            </tr>
            <tr>
              <th>32</th>
              <td>SOLOS</td>
              <td>MapServer</td>
            </tr>
            <tr>
              <th>33</th>
              <td>USO</td>
              <td>MapServer</td>
            </tr>
            <tr>
              <th>34</th>
              <td>veg_mural</td>
              <td>MapServer</td>
            </tr>
            <tr>
              <th>35</th>
              <td>VEGETACAO</td>
              <td>MapServer</td>
            </tr>
          </tbody>
        </table>
        </div>
        <br />
        <br />


.. code-block:: default


    arcgis.search(where="folders")






.. only:: builder_html

    .. raw:: html

        <div>
        <style scoped>
            .dataframe tbody tr th:only-of-type {
                vertical-align: middle;
            }

            .dataframe tbody tr th {
                vertical-align: top;
            }

            .dataframe thead th {
                text-align: right;
            }
        </style>
        <table border="1" class="dataframe">
          <thead>
            <tr style="text-align: right;">
              <th></th>
              <th>0</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <th>0</th>
              <td>Utilities</td>
            </tr>
          </tbody>
        </table>
        </div>
        <br />
        <br />

For example, in our case, the geometries for highways, railways
and hidrographies is in the service folder called BASEMAP.

Inside the folder there are various layers, and we will also need those.

The layer number for railway is 2, for highways is 3 and for hidrographies
is 4.

The function :py:func:`mapsbr.arcgis.get_map` takes arguments for all these
things. But by default, it will search in an IBGE host, so you just need to pass
the service and layer identifiers.


.. code-block:: default


    railways = arcgis.get_map("BASEMAP", layer=2)
    highways = arcgis.get_map("BASEMAP", layer=3)
    hidrographies = arcgis.get_map("BASEMAP", layer=4)

    transports = railways, highways, hidrographies
    titles = ["Railways", "Highways", "Hidrographies"]








Once we have it, let's now plot it.


.. code-block:: default


    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(15, 10))
    br = ibgemaps.get_map("BR")
    for ax, transport, title in zip(axes.flat, transports, titles):
        br.plot(ax=ax, color="white", edgecolor="gray")
        transport.plot(ax=ax, column=transport.columns[1])
        ax.set_title(title)
        ax.axis("off")



.. image:: /gallery/images/sphx_glr_plot_hidrographies_and_roads_001.png
    :class: sphx-glr-single-img






.. rst-class:: sphx-glr-timing

   **Total running time of the script:** ( 0 minutes  10.851 seconds)

**Estimated memory usage:**  121 MB


.. _sphx_glr_download_gallery_plot_hidrographies_and_roads.py:


.. only :: html

 .. container:: sphx-glr-footer
    :class: sphx-glr-footer-example



  .. container:: sphx-glr-download

     :download:`Download Python source code: plot_hidrographies_and_roads.py <plot_hidrographies_and_roads.py>`



  .. container:: sphx-glr-download

     :download:`Download Jupyter notebook: plot_hidrographies_and_roads.ipynb <plot_hidrographies_and_roads.ipynb>`


.. only:: html

 .. rst-class:: sphx-glr-signature

    `Gallery generated by Sphinx-Gallery <https://sphinx-gallery.github.io>`_

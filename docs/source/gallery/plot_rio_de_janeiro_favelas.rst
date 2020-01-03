.. note::
    :class: sphx-glr-download-link-note

    Click :ref:`here <sphx_glr_download_gallery_plot_rio_de_janeiro_favelas.py>` to download the full example code
.. rst-class:: sphx-glr-example-title

.. _sphx_glr_gallery_plot_rio_de_janeiro_favelas.py:


Favelas in Rio de Janeiro
=========================

This is another example in which we use data from the
ArcGIS server of Rio de Janeiro city.

This time, we'll try to visualize the distribution of slums or favelas
in the city.

Let's first try to get the map of the city and afterwards plot the favelas
geometries.


.. code-block:: default


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








Now, just to see what other interesting things we can do with GeoPandas
and the Shapely library in general: let's calculate the area of the geometry!

This will give us a rough idea about which favela is the biggest:


.. code-block:: default


    favelas["area"] = favelas.geometry.area
    favelas = favelas.sort_values("area", ascending=False)

    favelas






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
              <th>geometry</th>
              <th>Nome</th>
              <th>area</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <th>492</th>
              <td>POLYGON ((-43.49245 -22.86656, -43.49246 -22.8...</td>
              <td>Fazenda Coqueiro</td>
              <td>1.015599e-04</td>
            </tr>
            <tr>
              <th>538</th>
              <td>POLYGON ((-43.58956 -22.89900, -43.59166 -22.8...</td>
              <td>Nova Cidade</td>
              <td>8.160836e-05</td>
            </tr>
            <tr>
              <th>937</th>
              <td>MULTIPOLYGON (((-43.24500 -22.99100, -43.24506...</td>
              <td>Rocinha</td>
              <td>7.385933e-05</td>
            </tr>
            <tr>
              <th>870</th>
              <td>POLYGON ((-43.33619 -22.97368, -43.33656 -22.9...</td>
              <td>Rio das Pedras</td>
              <td>5.048410e-05</td>
            </tr>
            <tr>
              <th>326</th>
              <td>MULTIPOLYGON (((-43.26751 -22.85952, -43.26751...</td>
              <td>Morro do Alemão</td>
              <td>4.539358e-05</td>
            </tr>
            <tr>
              <th>...</th>
              <td>...</td>
              <td>...</td>
              <td>...</td>
            </tr>
            <tr>
              <th>703</th>
              <td>POLYGON ((-43.30936 -23.00281, -43.30935 -23.0...</td>
              <td>Ilha da Gigóia - Lote 500</td>
              <td>7.756680e-08</td>
            </tr>
            <tr>
              <th>288</th>
              <td>POLYGON ((-43.24877 -22.85345, -43.24873 -22.8...</td>
              <td>Avenida dos Campeões - Praça Elói de Andrade</td>
              <td>7.395546e-08</td>
            </tr>
            <tr>
              <th>239</th>
              <td>POLYGON ((-43.25576 -22.88969, -43.25605 -22.8...</td>
              <td>Engenheiro Alberto Moas, próxima ao nº 75</td>
              <td>5.387290e-08</td>
            </tr>
            <tr>
              <th>744</th>
              <td>MULTIPOLYGON (((-43.43338 -22.99409, -43.43338...</td>
              <td>Caminho do Bicho</td>
              <td>2.707933e-08</td>
            </tr>
            <tr>
              <th>717</th>
              <td>POLYGON ((-43.40292 -22.97429, -43.40303 -22.9...</td>
              <td>Vila Autódromo</td>
              <td>1.689168e-08</td>
            </tr>
          </tbody>
        </table>
        <p>1018 rows × 3 columns</p>
        </div>
        <br />
        <br />

Now, here is what I wanna do: highlight the five biggest ones.

This will be straight-forward to do with annotate method of matplotlib.


.. code-block:: default


    favelas["point"] = favelas.geometry.centroid  # calculate the center of the geometry

    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(10, 7))

    districts.plot(color="white", edgecolor="grey", alpha=0.3, ax=ax)
    favelas.plot(column="Nome", ax=ax)

    ax.axis("off")
    ax.set_title("Favelas in Rio de Janeiro city\nBiggest 5 highlighted")

    for _, row in favelas.head().iterrows():
        ax.annotate(
            row.Nome,
            xy=(row.point.x, row.point.y),
            xytext=(0, 1),
            textcoords="offset points",
        )



.. image:: /gallery/images/sphx_glr_plot_rio_de_janeiro_favelas_001.png
    :class: sphx-glr-single-img






.. rst-class:: sphx-glr-timing

   **Total running time of the script:** ( 0 minutes  9.505 seconds)

**Estimated memory usage:**  106 MB


.. _sphx_glr_download_gallery_plot_rio_de_janeiro_favelas.py:


.. only :: html

 .. container:: sphx-glr-footer
    :class: sphx-glr-footer-example



  .. container:: sphx-glr-download

     :download:`Download Python source code: plot_rio_de_janeiro_favelas.py <plot_rio_de_janeiro_favelas.py>`



  .. container:: sphx-glr-download

     :download:`Download Jupyter notebook: plot_rio_de_janeiro_favelas.ipynb <plot_rio_de_janeiro_favelas.ipynb>`


.. only:: html

 .. rst-class:: sphx-glr-signature

    `Gallery generated by Sphinx-Gallery <https://sphinx-gallery.github.io>`_

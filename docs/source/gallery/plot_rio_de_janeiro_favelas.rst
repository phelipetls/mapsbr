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

    favelas.head(20)






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
              <td>0.000102</td>
            </tr>
            <tr>
              <th>538</th>
              <td>POLYGON ((-43.58956 -22.89900, -43.59166 -22.8...</td>
              <td>Nova Cidade</td>
              <td>0.000082</td>
            </tr>
            <tr>
              <th>937</th>
              <td>MULTIPOLYGON (((-43.24500 -22.99100, -43.24506...</td>
              <td>Rocinha</td>
              <td>0.000074</td>
            </tr>
            <tr>
              <th>870</th>
              <td>POLYGON ((-43.33619 -22.97368, -43.33656 -22.9...</td>
              <td>Rio das Pedras</td>
              <td>0.000050</td>
            </tr>
            <tr>
              <th>326</th>
              <td>MULTIPOLYGON (((-43.26751 -22.85952, -43.26751...</td>
              <td>Morro do Alemão</td>
              <td>0.000045</td>
            </tr>
            <tr>
              <th>...</th>
              <td>...</td>
              <td>...</td>
              <td>...</td>
            </tr>
            <tr>
              <th>381</th>
              <td>POLYGON ((-43.31591 -22.85675, -43.31599 -22.8...</td>
              <td>Morro do Juramento</td>
              <td>0.000027</td>
            </tr>
            <tr>
              <th>384</th>
              <td>MULTIPOLYGON (((-43.33766 -22.81993, -43.33782...</td>
              <td>Vila Rica de Irajá</td>
              <td>0.000027</td>
            </tr>
            <tr>
              <th>463</th>
              <td>MULTIPOLYGON (((-43.29018 -22.85078, -43.29023...</td>
              <td>Vila Proletária da Penha</td>
              <td>0.000027</td>
            </tr>
            <tr>
              <th>627</th>
              <td>POLYGON ((-43.63739 -22.91760, -43.63786 -22.9...</td>
              <td>Divinéia</td>
              <td>0.000027</td>
            </tr>
            <tr>
              <th>936</th>
              <td>POLYGON ((-43.24515 -22.99559, -43.24630 -22.9...</td>
              <td>Vidigal</td>
              <td>0.000026</td>
            </tr>
          </tbody>
        </table>
        <p>20 rows × 3 columns</p>
        </div>
        <br />
        <br />

Now, here is what I wanna do: highlight the five biggest ones.

This will be straight-forward to do with annotate method of matplotlib.


.. code-block:: default


    favelas["point"] = favelas.geometry.centroid  # calculate the center of the geometry

    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(10, 5))

    districts.plot(color="white", edgecolor="lightgray", ax=ax)
    favelas.plot(color="black", ax=ax)
    favelas.query("Nome in @favelas.Nome.head()").plot(color="tab:orange", ax=ax)

    ax.axis("off")
    ax.set_title("Favelas in Rio de Janeiro city\nBiggest 5 in area highlighted")

    for _, row in favelas.head().iterrows():
        ax.annotate(
            row.Nome,
            xy=(row.point.x, row.point.y),
            xytext=(5, 10),
            textcoords="offset points",
            arrowprops=dict(
                arrowstyle="->", color="black", ls="--", connectionstyle="angle3"
            ),
            bbox=dict(boxstyle="round", alpha=0.8, facecolor="white"),
            color="k", fontsize="small"
        )



.. image:: /gallery/images/sphx_glr_plot_rio_de_janeiro_favelas_001.png
    :class: sphx-glr-single-img






.. rst-class:: sphx-glr-timing

   **Total running time of the script:** ( 0 minutes  8.302 seconds)

**Estimated memory usage:**  105 MB


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

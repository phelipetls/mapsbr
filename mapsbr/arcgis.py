import pandas as pd
import geopandas as gpd
from shapely.geometry import shape
from .helpers.request import get_geojson


def get_map(service, baseurl=None, service_type="MapServer", layer=0):
    """
    Get geometries associated with an ARCGIS url.

    Parameters
    ----------
    service : str
        Service identifier, part of the url
        after "services/"

    baseurl : str, default None
        Base url or host. By default, it will
        be https://mapasinterativos.ibge.gov.br/arcgis/rest/services

    service_type : str, default "MapServer"
        Service type

    layer : int or str, default 0
        Service layer

    Returns
    -------
    GeoDataFrame
    """
    maps = pd.concat(
        get_all_features(service, baseurl, service_type, layer), axis="rows"
    )
    return gpd.GeoDataFrame(maps)


def build_url(service, baseurl=None, service_type="MapServer", layer=0, count=0):
    """
    Helper function to build valid ARCGIS url.
    """
    if baseurl is None:
        baseurl = "https://mapasinterativos.ibge.gov.br/arcgis/rest/services"
    baseurl = baseurl.rstrip("/")
    where = f"where=objectId>={count}+and+objectId<{count+1000}"
    return f"{baseurl}/{service}/{service_type}/{layer}/query?{where}&f=geojson"


def get_all_features(service, baseurl=None, service_type="MapServer", layer=0):
    """
    Helper function to get all features from a
    service layer. This is a work around the response's
    1000 row limit.
    """
    count = 0
    while True:
        url = build_url(service, baseurl, service_type, layer, count=count)
        geojson = get_geojson(url)
        if geojson["features"]:
            yield pd.DataFrame(read_geojson(geojson))
            count += 1000
        else:
            break


def read_geojson(geojson):
    """
    Helper function to read GeoJSON to
    get all geometries and properties.
    """
    property_dict = geojson["features"][0].get("properties", "property")
    property_name = list(property_dict)[0]
    return [
        {
            "geometry": shape(feature["geometry"]),
            property_name: list(feature["properties"].values())[0],
        }
        for feature in geojson["features"]
    ]


def search(baseurl=None, where="services"):
    """
    Search available resources in a given host.

    Parameters
    ----------
    baseurl : str, default None
        Base url or host. By default, it will
        be https://mapasinterativos.ibge.gov.br/arcgis/rest/services

    where : str, default "services"
        Where to search, valid values are "folders" or "services"

    Returns
    -------
    DataFrame
    """
    if baseurl is None:
        baseurl = "https://mapasinterativos.ibge.gov.br/arcgis/rest/services"
    services = get_geojson(f"{baseurl}?f=json")[where]
    return pd.DataFrame(services)

# vi: nowrap

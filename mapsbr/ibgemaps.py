import shapely
import numpy as np
import geopandas as gpd
from .helpers import utils, ibgetools
from .helpers.request import get_geojson


def get_map(location, including=None, geolevel="states"):
    """
    Get and turn a GeoJSON of a IBGE
    location into a GeoSeries.

    Parameters
    ----------
    location : int or str
        Location identifier (code or string)
        as in IBGE.

    including : str, default None
        Map level of detail, e.g. "cities" etc.
        By default, no details.

    Returns
    -------
    GeoSeries
        A GeoSeries with shapely objects only.
    """
    if isinstance(location, str) and location != "BR":
        location = ibgetools.ibge_encode(location, geolevel)
    url = build_url(location, including)
    geojson = get_geojson(url)
    parsed_geojson = parse_geojson(geojson, including)
    return gpd.GeoDataFrame(parsed_geojson)


def build_url(code, including=None):
    """
    Helper function to build valid URL
    for IBGE API.
    """
    baseurl = "http://servicodados.ibge.gov.br/api/v2/malhas/"
    resolution = resolutions.get(including, 0)
    url = f"{baseurl}{code}?resolucao={resolution}&formato=application/vnd.geo+json"
    return url


resolutions = {
    "macrorregioes": 1,
    "macroregions": 1,
    "estados": 2,
    "states": 2,
    "mesorregioes": 3,
    "mesoregions": 3,
    "microrregioes": 4,
    "microregions": 4,
    "municipios": 5,
    "municipalities": 5,
}


def parse_geojson(geojson):
    features = utils.get_features(geojson)
    return [
        {
            "geometry": shapely.geometry.shape(feature["geometry"])
        }
        for feature in features
    ]


@np.vectorize
def geocode(location, geolevel="states"):
    """
    Vectorized function to turn location
    code or name into its corresponding
    geometric shapely object.

    Parameters
    ----------
    locations : str, iterables, Series, GeoSeries
        Series with locations' names
    """
    if utils.assert_number(location) and location != "BR":
        location = ibgetools.ibge_encode(location, geolevel)
    url = build_url(location)
    geojson = get_geojson(url)
    features = utils.get_features(geojson)
    return shapely.geometry.shape(features[0]["geometry"])

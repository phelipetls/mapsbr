import shapely
import numpy as np
import geopandas as gpd
from .tools import geocode
from .helpers import utils
from .helpers.request import get_geojson


def get_map(location, geo="states", include=None):
    """
    Get and turn a GeoJSON of a IBGE
    location into a GeoSeries.

    Parameters
    ----------
    location : int or str
        Location identifier (code or string)
        as in IBGE.

    include : str, default None
        Map level of detail, e.g. "cities" etc.
        By default, no details.

    Returns
    -------
    GeoSeries
        A GeoSeries with shapely objects only.
    """
    if isinstance(location, str) and location != "BR":
        location = geocode(location, geo)
    url = build_url(location, include)
    geojson = get_geojson(url)
    return gpd.GeoDataFrame(read_geojson(geojson))


def build_url(code, include=None):
    """
    Helper function to build valid URL
    for IBGE API.
    """
    baseurl = "http://servicodados.ibge.gov.br/api/v2/malhas/"
    resolution = resolutions.get(include, 0)
    url = f"{baseurl}{code}?resolucao={resolution}&formato=application/vnd.geo+json"
    return url


resolutions = {
    "macroregions": 1,
    "states": 2,
    "mesoregions": 3,
    "microregions": 4,
    "cities": 5,
}


def read_geojson(geojson):
    features = utils.get_features(geojson)
    return [
        {
            "location": feature["properties"]["codarea"],
            "geometry": shapely.geometry.shape(feature["geometry"])
        }
        for feature in features
    ]


@np.vectorize
@utils.memoize
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
        location = ibge_encode(location, geolevel)
    url = build_url(location)
    geojson = get_geojson(url)
    features = utils.get_features(geojson)
    return shapely.geometry.shape(features[0]["geometry"])

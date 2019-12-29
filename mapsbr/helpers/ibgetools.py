from . import utils
from .request import get_geojson


def ibge_encode(locations, geolevel):
    """
    Vectorized function to turn locations
    names into their corresponding IBGE code.

    Parameters
    ----------
    locations : str, iterables, Series, GeoSeries
        Series with locations' names.

    geolevel : str, default "states"
        Geographic level, e.g. "estados", "mesoregions".

    Returns
    -------
    ndarray

    Raises
    ------
    AssertionError
        If try to pass numbers or strings as numbers.

    ValueError
        If invalid geographic level is passed.
    """
    err_msg = "Cannot encode numbers or strings representing numbers"
    assert all([utils.assert_number(location) for location in locations]), err_msg
    locations_dict = map_name_to_code(geolevel)
    return utils.vectorized_get(locations_dict, locations)


def ibge_decode(locations, geolevel):
    """
    Vectorized function to turn locations
    codes into their corresponding IBGE name.

    Parameters
    ----------
    locations : str, iterables, Series, GeoSeries
        Series with locations' codes.

    geolevel : str
        Geographic level, e.g. "estados", "mesoregions".

    Returns
    -------
    ndarray

    Raises
    ------
    AssertionError
        If try to pass numbers or strings as numbers.

    ValueError
        If invalid geographic level is passed.
    """
    try:
        locations = [int(location) for location in locations]
    except ValueError:
        raise ValueError("Cannot decode numbers")
    locations_dict = map_code_to_name(geolevel)
    return utils.vectorized_get(locations_dict, locations)


def map_name_to_code(geolevel):
    """
    Make dictionary to map location name
    to IBGE code.
    """
    url = build_url(geolevel)
    locations = get_geojson(url)
    return {location["nome"]: location["id"] for location in locations}


def map_code_to_name(geolevel):
    """
    Make dictionary to map location code
    to IBGE name.
    """
    url = build_url(geolevel)
    locations = get_geojson(url)
    return {location["id"]: location["nome"] for location in locations}


def build_url(geolevel):
    baseurl = "https://servicodados.ibge.gov.br/api/v1/localidades/"
    location = arguments_dict.get(geolevel, None)
    if location is None:
        raise ValueError(f"{geolevel.capitalize()} is not a valid geographic level")
    url = f"{baseurl}{location}"
    return url


arguments_dict = {
    "estado": "estados",
    "estados": "estados",
    "state": "estados",
    "states": "estados",
    "mesorregiao": "mesorregioes",
    "mesorregioes": "mesorregioes",
    "mesoregion": "mesorregioes",
    "mesoregions": "mesorregioes",
    "macrorregiao": "regioes",
    "macorregioes": "regioes",
    "macroregion": "regioes",
    "macroregions": "regioes",
    "microrregiao": "microrregioes",
    "microrregioes": "microrregioes",
    "microregion": "microrregioes",
    "microregions": "microrregioes",
    "municipio": "municipios",
    "municipios": "municipios",
    "municipality": "municipios",
    "municipality": "municipios",
}

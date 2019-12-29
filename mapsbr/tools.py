from .helpers import utils
from .helpers.request import get_geojson


def geocode(locations, geo="states"):
    """
    Vectorized function to turn locations
    names into their corresponding IBGE code.

    Parameters
    ----------
    locations : str, iterables, Series, GeoSeries
        Series with locations' names.

    geo : str, default "states"
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
    err_msg = "Numbers or strings representing digits cannot be a location name"
    assert all([utils.assert_number(location) for location in locations]), err_msg
    locations_dict = map_name_to_code(geo)
    return utils.vectorized_get(locations_dict, locations)


def map_name_to_code(geo):
    """
    Make dictionary to map location name
    to IBGE code.
    """
    url = build_url(geo)
    locations = get_geojson(url)
    return {location["nome"]: location["id"] for location in locations}


def build_url(geo):
    baseurl = "https://servicodados.ibge.gov.br/api/v1/localidades/"
    location = arguments_dict.get(geo, None)
    if location is None:
        raise ValueError(f"{geo.capitalize()} is not a valid geographic level")
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

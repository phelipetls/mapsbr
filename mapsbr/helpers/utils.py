import numpy as np


def memoize(function):
    cache = {}

    def decorated_function(arg, *args, **kwargs):
        if arg not in cache:
            cache[arg] = function(arg, *args, **kwargs)
        return cache[arg]
    return decorated_function


@np.vectorize
def vectorized_get(dictionary, key):
    return dictionary.get(key, False)


@np.vectorize
def is_number(x):
    try:
        int(x)
        return False
    except ValueError:
        return True


def get_features(geojson):
    try:
        features = geojson["features"]
    except KeyError:
        raise KeyError(f"{geojson} is an invalid GeoJSON. Not a feature collection")
    return features

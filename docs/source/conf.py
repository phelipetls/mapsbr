# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))
sys.path.insert(0, os.path.abspath('../../../seriesbr'))

# -- Project information -----------------------------------------------------

project = 'mapsbr'
copyright = '2019, Phelipe Teles'
author = 'Phelipe Teles'

# The full version, including alpha/beta/rc tags
release = '0.0.2'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx_gallery.gen_gallery",
    "IPython.sphinxext.ipython_directive",
    "IPython.sphinxext.ipython_console_highlighting",
    "matplotlib.sphinxext.plot_directive",
]

# Sphinx-Gallery configuration
sphinx_gallery_conf = {
    "examples_dirs": "examples",  # path to your example scripts
    "gallery_dirs": "gallery",  # path to where to save gallery generated output
    'show_memory': True,
}

import warnings

warnings.filterwarnings("ignore", category=UserWarning,
                        message='Matplotlib is currently using agg, which is a'
                                ' non-GUI backend, so cannot show the figure.')

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinxdoc'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# The master toctree document.
master_doc = 'index'

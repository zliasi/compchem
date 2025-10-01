# Configuration file for Sphinx documentation

import os
import sys

# Project information
project = 'compchem'
copyright = '2025, Zacharias Liasi'
author = 'Zacharias Liasi'
release = '0.1.0'

# General configuration
extensions = [
    'myst_parser',  # Markdown support
    'sphinx.ext.mathjax',  # Math support
    'sphinx.ext.githubpages',  # GitHub Pages support
]

# Markdown support
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

myst_enable_extensions = [
    "colon_fence",  # ::: instead of ```
    "deflist",
    "html_image",
]

templates_path = ['_templates']
exclude_patterns = []

# HTML output options
#html_theme = 'sphinx_rtd_theme'  

#html_theme_options = {
#    'navigation_depth': 3,
#    'collapse_navigation': False,
#}

html_theme = 'pydata_sphinx_theme'

html_theme_options = {
    "github_url": "https://github.com/zliasi/compchem",
    "show_nav_level": 2,
    "navigation_depth": 3,
}


html_static_path = ['_static']
html_title = "Introduction to computational chemistry"

# GitHub Pages: create .nojekyll file
html_extra_path = ['.nojekyll']

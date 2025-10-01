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
    'myst_parser',
    'sphinx.ext.mathjax',
    'sphinx.ext.githubpages',
]

# Markdown support
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "html_image",
]

templates_path = ['_templates']
exclude_patterns = []

# HTML output options
html_theme = 'pydata_sphinx_theme'

html_theme_options = {
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/zliasi/compchem",
            "icon": "fab fa-github-square",
        },
    ],
    "navbar_end": ["navbar-icon-links"],
    "show_toc_level": 2,
    "navigation_depth": 3,
}

html_static_path = ['_static']
html_title = "Introduction to computational chemistry"

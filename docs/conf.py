import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'AIStack'
author = 'Ersin Akşar'
release = '1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo',
    'sphinx.ext.ifconfig',
    'sphinx.ext.githubpages',
    'sphinx.ext.intersphinx',
    'sphinx.ext.extlinks',
    'sphinx.ext.doctest',
    'sphinx.ext.mathjax',
    'sphinx.ext.imgmath',
    'sphinx.ext.graphviz',
    'sphinx.ext.inheritance_diagram',
    'sphinx_copybutton',
    'sphinxcontrib.mermaid',
    'pydata_sphinx_theme',
]

html_theme = 'pydata_sphinx_theme'

html_theme_options = {
    'navbar_start': ['navbar-logo'],
    'navbar_center': ['navbar-nav'],
    'navbar_end': ['navbar-icon-links'],
    'primary_sidebar_end': ['sidebar-ethical-ads'],
}

locale_dirs = ['locale/']
gettext_compact = False
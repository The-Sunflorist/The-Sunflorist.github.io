# coding=utf-8
#
# conf.py
# The-Sunflorist.github.io/
#
# Created by 向阳花花农(The Sunflorist) on 2024-11-22.
# Copyright © 2024 向阳花花农(The Sunflorist). All rights reserved.
#
# Configuration file for the Sphinx documentation builder.
# https://www.sphinx-doc.org/en/master/usage/configuration.html


import sys
from datetime import datetime

# project information
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = '向阳花花农的花海'
author = '向阳花花农'
copyright = (
    f'《向阳花花农的花海》 © {(now := datetime.now()).year} 由向阳花花农创作，遵循CC BY-NC-SA 4.0协议，保留所有版权。\n'
    "The Sunflorist's Shangri-La © 2024 by The Sunflorist is licensed under CC BY-NC-SA 4.0, all rights reserved."
)
project_copyright = copyright
release = now.strftime(format='%Y.%m.%d%H%M')
version = now.strftime(format='%Y.%m')

# general configuration
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# https://www.sphinx-doc.org/en/master/usage/extensions/index.html
extensions = [
    'sphinx.ext.duration',  # show duration for building each file
    'sphinx.ext.mathjax',  # render LaTeX to JavaScript
    'sphinxcontrib.googleanalytics',  # Google Analytics
    'sphinx_copybutton',  # copy button for code
    'myst_parser',  # parse extended markdown
]

today_fmt = '%Y-%m-%d %H:%M:%S UTC %z'

templates_path = ['_templates']
exclude_patterns = ['.DS_Store', '.idea', '.tmp', '_static', '_templates', 'aux', '_images', 'src', 'README.md']

language = 'zh_CN'
gettext_compact = False

# MyST options
# https://myst-parser.readthedocs.io/en/latest/index.html

# https://myst-parser.readthedocs.io/en/latest/syntax/optional.html
myst_enable_extensions = [
    'dollarmath',  # dollar sign for latex
    'html_image',  # html img tag
    'substitution',  # substitution text
]
# https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#substitutions-with-jinja2
myst_substitutions = {
    'more': r'<i class="em-svg em-hibiscus" aria-role="presentation" aria-label="HIBISCUS"></i> 余香',
    'music': r'<i class="em-svg em-musical_score" aria-role="presentation" aria-label="MUSICAL SCORE"></i> 原曲',
    'idea': r'<i class="em-svg em-star2" aria-role="presentation" aria-label="GLOWING STAR"></i> 灵感',
    'meaning': r'<i class="em-svg em-mag" aria-role="presentation" aria-label="LEFT-POINTING MAGNIFYING GLASS"></i> 大意',
}

# HTML options
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_title = project
html_static_path = ['_static']
html_theme_options = {
    'announcement': r'<i class="em-svg em-tada" aria-role="presentation" '
                    r'aria-label="PARTY POPPER"></i> Bravo! 恭喜你觅得一处桃花源！',
    'light_logo': 'sun_light_500x500.gif',
    'dark_logo': 'sun_dark_500x500.gif',
    'top_of_page_buttons': [],
}
html_favicon = '_static/sun_100x100.png'

# https://dailystuff.nl/blog/2023/adding-google-analytics-in-sphinx
googleanalytics_id = 'G-J355ELCH1B' if 'readthedocs' in sys.path[0] else 'G-GVGCSPC1K4'

# todo: EPUB options
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-epub-output

epub_description = '因为喜欢，所以种向日葵。He grows sunflowers out of passion.'
epub_identifier = 'The-Sunflorists-Shangri-La'
epub_cover = ('aux/book_cover.png', '')
epub_tocdepth = 6
epub_tocscope = 'includehidden'
epub_show_urls = 'no'

# todo: LaTeX options
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-latex-output

# (startdocname, targetname, title, author, theme, toctree_only)
# latex_documents = ()

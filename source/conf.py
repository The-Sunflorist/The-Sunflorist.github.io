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


import os
import sys
from datetime import datetime

# note: non-Sphinx configurations are prefixed with an `_`, but not compulsory
_now = datetime.now().astimezone()
_year = _now.year
_on_read_the_docs = 'readthedocs' in sys.path[0]

_project_zh = '向阳花花农的花海'
_project_en = "The Sunflorist's Shangri-La"
_author_zh = '向阳花花农'
_author_en = 'The Sunflorist'

_license = 'CC BY-NC-SA 4.0'
_copyright_zh = (
    f'《{_project_zh}》© {_year} 由{_author_zh}创作，遵循{_license}协议，保留所有版权。'
)
_copyright_en = (
    f"{_project_en} © {_year} by {_author_en} is licensed under {_license},"
    f" all rights reserved."
)

_description_zh = '因为喜欢，所以种向日葵。'
_description_en = 'He grows sunflowers out of passion.'

# -----------------------------------------------------------------------------
# project information: https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information # noqa

project = _project_zh
author = _author_zh

copyright = f'{_copyright_zh}{_copyright_en}'  # noqa
project_copyright = copyright

release = _now.strftime(format='%Y.%m.%d%H%M')
version = _now.strftime(format='%Y.%m')

# -----------------------------------------------------------------------------
# general configuration: https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration # noqa

# Sphinx extensions: https://www.sphinx-doc.org/en/master/usage/extensions/index.html # noqa
extensions = [
    'myst_nb',  # parse jupyter notebook and myst markdown
    'sphinx.ext.duration',  # show duration for building each file
    'sphinx.ext.mathjax',  # render LaTeX to JavaScript
    'sphinxcontrib.googleanalytics',  # Google Analytics
    'sphinx_copybutton',  # copy button for code
    'sphinx_design',  # screen-size responsive web-components
]

# Sphinx uses `time` instead of `datetime` package,
# `time` does not support `%:z` currently
today_fmt = '%Y-%m-%d %H:%M:%S %Z'

# todo
# templates_path = ['_templates']
exclude_patterns = [
    '.DS_Store', '.idea', 'build',
    '_images', '_pythons', '_static', '_templates',
    'aux',
    'README.md',
]

language = 'zh_CN'
_html_language = language.replace('_', '-')

gettext_compact = False

# -----------------------------------------------------------------------------
# MyST options: https://myst-parser.readthedocs.io/en/latest/index.html

# MyST extensions: https://myst-parser.readthedocs.io/en/latest/syntax/optional.html # noqa
myst_enable_extensions = [
    'attrs_block',  # add html attributes for inline contents
    'attrs_inline',  # add html attributes for block contents
    'colon_fence',  # use colons instead of backticks for directives
    'dollarmath',  # dollar sign for latex
    'html_image',  # html img tag
    'substitution',  # substitution text
]

myst_links_external_new_tab = True

myst_html_meta = {
    f'author lang={_html_language}': _author_zh,
    f'copyright lang={_html_language}': _copyright_zh,
    'author lang=en': _author_en,
    'copyright lang=en': _copyright_en,
}

myst_number_code_blocks = ['python', 'markdown']

# https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#substitutions-with-jinja2 # noqa
myst_substitutions = {
    'zh': r'<i class="em-svg em-mahjong" aria-role="presentation" '
          r'aria-label="MAHJONG TILE RED DRAGON"></i> 中文',
    'en': r'<i class="em-svg em-abcd" aria-role="presentation" '
          r'aria-label="INPUT SYMBOL FOR LATIN SMALL LETTERS"></i> English',
    'more': r'<i class="em-svg em-hibiscus" aria-role="presentation" '
            r'aria-label="HIBISCUS"></i> 余香',
    'music': r'<i class="em-svg em-musical_score" aria-role="presentation" '
             r'aria-label="MUSICAL SCORE"></i> 原曲',
    'idea': r'<i class="em-svg em-star2" aria-role="presentation" '
            r'aria-label="GLOWING STAR"></i> 灵感',
    'meaning': r'<i class="em-svg em-mag" aria-role="presentation" '
               r'aria-label="LEFT-POINTING MAGNIFYING GLASS"></i> 大意',
}

# -----------------------------------------------------------------------------
# HTML options: https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output # noqa

html_title = project
html_favicon = '_static/logos/sun_100x100.png'

html_static_path = ['_static']

html_theme = 'furo'
html_theme_options = {
    'announcement': r'<i class="em-svg em-tada" aria-role="presentation" '
                    r'aria-label="PARTY POPPER"></i> Bravo! 恭喜你觅得一处桃花源！',
    'light_logo': 'logos/sun_light_500x500.gif',
    'dark_logo': 'logos/sun_dark_500x500.gif',
    'top_of_page_buttons': [],
}

html_css_files = ['https://emoji-css.afeld.me/emoji.css']
html_js_files = []

_envs_path = (
    '/home/docs/checkouts/readthedocs.org/user_builds/the-sunflorist'
) if _on_read_the_docs else f'{os.path.expanduser('~')}/miniconda3'
_jieba_dict_path = '/envs/latest/lib/python3.13/site-packages/jieba/dict.txt'
html_search_options = {
    'dict': f'{_envs_path}{_jieba_dict_path}'
}

# https://dailystuff.nl/blog/2023/adding-google-analytics-in-sphinx
googleanalytics_id = 'G-J355ELCH1B' if _on_read_the_docs else 'G-GVGCSPC1K4'

# -----------------------------------------------------------------------------
# todo: EPUB options: https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-epub-output # noqa

epub_description = f'{_description_zh}{_description_en}'
epub_identifier = _project_en.replace(' ', '-').replace("'", '')
epub_cover = ('aux/book_cover.png', '')
epub_tocdepth = 6
epub_tocscope = 'includehidden'
epub_show_urls = 'no'

# -----------------------------------------------------------------------------
# todo: LaTeX options: https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-latex-output # noqa

# (startdocname, targetname, title, author, theme, toctree_only)
# latex_documents = ()

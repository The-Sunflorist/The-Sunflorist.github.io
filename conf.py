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

## note: non-Sphinx configurations are prefixed with an `_` for distinguishing, not compulsory
_now = datetime.now().astimezone()
_year = _now.year
_on_read_the_docs = 'readthedocs' in sys.path[0]

## project information: https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

_project_en = "The Sunflorist's Shangri-La"
_project_zh = '向阳花花农的花海'
project = _project_zh

_author_zh = '向阳花花农'
_author_en = 'The Sunflorist'
author = _author_zh

_license = 'CC BY-NC-SA 4.0'
_copyright_zh = f'《{_project_zh}》© {_year} 由{_author_zh}创作，遵循{_license}协议，保留所有版权。'
_copyright_en = f"{_project_en} © {_year} by {_author_en} is licensed under {_license}, all rights reserved."
copyright = f'{_copyright_zh}{_copyright_en}'
project_copyright = copyright

release = _now.strftime(format='%Y.%m.%d%H%M')
version = _now.strftime(format='%Y.%m')

## general configuration: https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Sphinx extensions: https://www.sphinx-doc.org/en/master/usage/extensions/index.html
extensions = [
    'myst_nb',  # parse jupyter notebook and myst markdown
    'sphinx.ext.duration',  # show duration for building each file
    'sphinx.ext.mathjax',  # render LaTeX to JavaScript
    'sphinxcontrib.googleanalytics',  # Google Analytics
    'sphinx_copybutton',  # copy button for code
    'sphinx_design',  # screen-size responsive web-components
]

# Sphinx uses `time` instead of `datetime` package, `time` does not support `%:z` currently
today_fmt = '%Y-%m-%d %H:%M:%S %Z'

# todo
# templates_path = ['_templates']
exclude_patterns = ['.DS_Store', '.idea', '.tmp', '_images', '_static', '_templates', 'aux', 'src', 'README.md']

language = 'zh_CN'
_html_language = language.replace('_', '-')

gettext_compact = False

## MyST options: https://myst-parser.readthedocs.io/en/latest/index.html

# MyST extensions: https://myst-parser.readthedocs.io/en/latest/syntax/optional.html
myst_enable_extensions = [
    'attrs_block',  # add html attributes for inline contents
    'attrs_inline',  # add html attributes for block contents
    'colon_fence',  # use colons instead of backticks for directives
    'dollarmath',  # dollar sign for latex
    'html_image',  # html img tag
    'substitution',  # substitution text
]

myst_links_external_new_tab = True

_description_zh = '因为喜欢，所以种向日葵。'
_description_en = 'He grows sunflowers out of passion.'

_keywords_zh = f'{_author_zh}, {_project_zh}, 向日葵, 阳光, 花海, 桃源, 桃花源, 世外桃源, 乌托邦, 诗歌, 歌词, 数字绘画'
_keywords_en = (f'{_author_en}, {_project_en}, sunflower, sunshine, shangri-la, arcadia, xanadu, peach garden, '
                f'utopia, poem, lyrics, digital drawing')

myst_html_meta = {
    f'author lang={_html_language}': _author_zh,
    f'description lang={_html_language}': _description_zh,
    f'keywords lang={_html_language}': _keywords_zh,
    f'copyright lang={_html_language}': _copyright_zh,

    'author lang=en': _author_en,
    'description lang=en': _description_en,
    'keywords lang=en': _keywords_en,
    'copyright lang=en': _copyright_en,
}

myst_number_code_blocks = ['python', 'markdown']

# https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#substitutions-with-jinja2
myst_substitutions = {
    'zh': r'<i class="em-svg em-mahjong" aria-role="presentation" aria-label="MAHJONG TILE RED DRAGON"></i> 中文',
    'en': r'<i class="em-svg em-abcd" aria-role="presentation" '
          r'aria-label="INPUT SYMBOL FOR LATIN SMALL LETTERS"></i> English',
    'more': r'<i class="em-svg em-hibiscus" aria-role="presentation" aria-label="HIBISCUS"></i> 余香',
    'music': r'<i class="em-svg em-musical_score" aria-role="presentation" aria-label="MUSICAL SCORE"></i> 原曲',
    'idea': r'<i class="em-svg em-star2" aria-role="presentation" aria-label="GLOWING STAR"></i> 灵感',
    'meaning': r'<i class="em-svg em-mag" aria-role="presentation" aria-label="LEFT-POINTING MAGNIFYING GLASS"></i> 大意',
}

## HTML options: https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = project
html_favicon = '_static/sun_100x100.png'

html_static_path = ['_static']

html_theme = 'furo'
html_theme_options = {
    'announcement': r'<i class="em-svg em-tada" aria-role="presentation" '
                    r'aria-label="PARTY POPPER"></i> Bravo! 恭喜你觅得一处桃花源！',
    'light_logo': 'sun_light_500x500.gif',
    'dark_logo': 'sun_dark_500x500.gif',
    'top_of_page_buttons': [],
}

html_css_files = ['https://emoji-css.afeld.me/emoji.css']
html_js_files = []

html_search_options = {
    'dict': f'{'/home/docs/checkouts/readthedocs.org/user_builds/the-sunflorist' if _on_read_the_docs
    else f'{os.path.expanduser('~')}/miniconda3'}/envs/latest/lib/python3.13/site-packages/jieba/dict.txt'
}

# https://dailystuff.nl/blog/2023/adding-google-analytics-in-sphinx
googleanalytics_id = 'G-J355ELCH1B' if _on_read_the_docs else 'G-GVGCSPC1K4'

## todo: EPUB options: https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-epub-output

epub_description = f'{_description_zh}{_description_en}'
epub_identifier = _project_en.replace(' ', '-').replace("'", '')
epub_cover = ('aux/book_cover.png', '')
epub_tocdepth = 6
epub_tocscope = 'includehidden'
epub_show_urls = 'no'

## todo: LaTeX options: https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-latex-output

# (startdocname, targetname, title, author, theme, toctree_only)
# latex_documents = ()

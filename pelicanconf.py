#!/usr/bin/env python
# -*- coding: utf-8 -*- #

'''
referência:: https://github.com/onur/medius/blob/demo/

'''


from __future__ import unicode_literals

AUTHOR = u'akarokr'
SITENAME = u'between the pages'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'pt'
STATIC_PATHS = ['img', 'img/favicon.png']

EXTRA_PATH_METADATA = {
    'img/favicon.png': {'path': 'favicon.png'}
}


THEME = u'themes/medius'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# LINKS
# LINKS = (('You can modify those links in your config file', '#'),)

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

# MENUITEMS = [(u'categories', u'pages/categories.html')]

# all defaults to True.
DISPLAY_HEADER = True
DISPLAY_FOOTER = True
DISPLAY_HOME = True
DISPLAY_MENU = True

MEDIUS_AUTHORS = {
    'Luiz Moura': {
        'description': """Blah""",
        'cover': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Milky_Way_Arch.jpg/1920px-Milky_Way_Arch.jpg',
        'image': 'https://github.com/akarokr/akarokr.github.io/raw/master/img/odin_valknut.webp',
        'links': (('github-square', 'https://github.com/akarokr'),
                  ('twitter-square', 'https://twitter.com/akarokr')),
    }
}

MEDIUS_CATEGORIES = {
    'dev': {
        'description': 'A galaxy is a gravitationally bound system of stars, stellar remnants, interstellar gas and dust, and dark matter.',
        'logo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/GalacticRotation2.svg/250px-GalacticRotation2.svg.png',
        'thumbnail': 'https://raw.githubusercontent.com/akarokr/akarokr.github.io/master/img/galaxia1.jpg'
    },
    'pelican': {
        'description': '',
        'logo': '',
        'thumbnail': 'https://raw.githubusercontent.com/akarokr/akarokr.github.io/master/img/galaxia2.jpg'
    }
}

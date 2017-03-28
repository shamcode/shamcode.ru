#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'shamcode'
SITENAME = u'shamcode'
SITEURL = u''

PATH = 'content'

TIMEZONE = 'Asia/Krasnoyarsk'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('github', 'https://github.com/shamcode'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# https://github.com/getpelican/pelican-plugins
PLUGIN_PATHS = ['pelican-plugins']

# https://github.com/alexandrevicenzi/Flex
THEME = "Flex"

# Enable i18n plugin.
PLUGINS = ['i18n_subsites']
# Enable Jinja2 i18n extension used to parse translations.
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n']
}

SITETITLE = u'shamcode'
SITELOGO = SITEURL + 'images/sham.jpg'
SITESUBTITLE = 'Developer'
BROWSER_COLOR = '#333'
ROBOTS = 'index, follow'

MENUITEMS = (('Архив', '/archives.html'),
             ('Категории', '/categories.html'),
             ('Тэги', '/tags.html'),)

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

MAIN_MENU = True

DEFAULT_LANG = u'ru'
OG_LOCALE = 'ru_RU'
LOCALE = 'ru_RU.UTF-8'

I18N_TEMPLATES_LANG = 'en'

from private_conf import *
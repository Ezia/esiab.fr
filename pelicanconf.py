#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Esia Belbachir'
SITENAME = 'Esia Belbachir'
AVATAR = '/images/avatar.png'

SITEDESCRIPTION = 'Étudiante en informatique'
LONGSITEDESCRIPTION = '''
<p>
Je suis étudiante ingénieure en informatique à l'Université de Technologie de Belfort-Montbéliard (UTBM) en France.
Je suis actuellement en double diplôme à l'Université du Québec à Chicoutimi (UQAC) en maîtrise informatique spécialité jeux vidéo. 
</p>
<p>
Ce site est en cours de construction, il sera complet dans très peu de temps.
</p>
'''

SITEURL = 'http://localhost:8000'
RELATIVE_URLS = False

THEME = 'pelican-breeze'

PATH = 'content'

TIMEZONE = 'America/Montreal'
DEFAULT_LANG = 'fr'
DEFAULT_DATE_FORMAT = ('%d/%m/%Y')

STATIC_PATHS = ['images', 'dl']

FAVICON = 'images/favicon.ico'

#############
# ATOM FEED #
#############

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None

############
# RSS FEED #
############

FEED_ALL_RSS = None
CATEGORY_FEED_RSS = None
TRANSLATION_FEED_RSS = None
AUTHOR_FEED_RSS = None

DISPLAY_SUMMARY = True

DEFAULT_CATEGORY = 'Miscellaneous'

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True

# Links
LINKS = [('Github', 'github', 'https://github.com/Ezia'),
         ('Email', 'envelope-o', 'mailto:esia.belbachir@protonmail.com'),]

DEFAULT_PAGINATION = 15

#################
# PLUGIN CONFIG #
#################

PLUGIN_PATHS = ['pelican-plugins']

PLUGINS = ['global_license']

# Other plugins to potentially add:
# 'pelicanfly',
# 'pelican_youtube',
# 'read_more_link',
# 'series',
# 'thumbnailer',


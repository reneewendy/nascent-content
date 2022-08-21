#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# Email protection
EMAIL_KEY = '^Ü;¤q\983t4¤Ï.²d¶`?h}p"+RËR®ÔpöÁÀ=Y.v¹Ýò>#Y²ßáéþ3yGÝR'
def encrypt(input):
	output = ''
	key = EMAIL_KEY
	l = len(key)
	for i in range(len(input)):
		output += chr(ord(input[i]) ^ ord(key[i%l]))
	return output


SITENAME = 'Headline'
SITESUBTITLE = 'Subtitle'
SITEURL = ''
ICON_URL= 'images/favicon.ico'
SITELOGO = 'images/logo.svg'
DEFAULT_BANNER_PIC = 'images/default_banner.png'

PATH = 'content'
THEME = '../Codeberg/NotMyIdea-Theme-Pelican/notmyidea/'
ALLOW_DARKTHEME = True
REMEMBER_DARKTHEME = True

TIMEZONE = 'Europe/Berlin'
DEFAULT_LANG = 'de'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS_WIDGET_NAME = 'Links'
LINKS = (('Impressum', '/pages/impressum'),
		 ('Datenschutzerklärung', '/pages/datenschutz'),
		 ('Design-Quellcode', 'https://codeberg.org/F_Thoma/NotMyIdea-Theme-Pelican'))

# Social widget
SOCIAL_WIDGET_NAME = 'Kontakt'
SOCIAL = (('Email', encrypt('mailto:email@example.org'), True),)

STATIC_PATHS = ['images']
PHOTOGRAPHER = 'Max Mustermann'
PHOTOGRAPHER_URL = 'https://de.wikipedia.org/wiki/Mustermann'



DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


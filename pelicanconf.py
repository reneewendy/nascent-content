AUTHOR = 'WendyRenee'
SITENAME = 'Markymark'
SITEURL = ''

# page path: static content. article paths: generated content.
PATH = 'content'
PAGE_PATHS = ['page']
ARTICLE_PATHS = ['article', 'darwin', 'stupid']
# PATH subdirectory content is also included.
# TODO: Add path to articles' html

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Darwin Awards', 'https://darwinawards.com/darwin/'),
         ('Honorable Mentions', 'https://darwinawards.com/stupid/'),
         ('Rules', 'https://darwinawards.com/rules/'),
         ('Slush', 'https://darwinawards.com/slush/new'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

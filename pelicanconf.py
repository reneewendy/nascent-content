AUTHOR = 'Wendy Northcutt'
SITENAME = 'Neo Darwin'
SITEURL = ''

PATH = 'content'
PAGE_PATHS = ['page']     # static content.
ARTICLE_PATHS = ['article', 'darwin', 'stupid', 'rules']     # generated content.

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
SOCIAL = (('Facebook Darwin', 'https://www.facebook.com/TheDarwinAwards'),
          ('Twitter Darwin', 'https://twitter.com/DarwinAwards'),
          ('Homepage Darwin', 'https://darwinawards.com'),)

THEME_TEMPLATES_OVERRIDES = ['themes/notmyidea/templates']  # works for base.html override

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

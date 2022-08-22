AUTHOR = 'Wendy Northcutt'
SITENAME = 'Reboot Darwin Awards'
SITESUBTITLE = 'giving humans the boot!'
SITEURL = ''
GITHUB_URL = 'https://github.com/reneewendy/nascent-content/blob/main/README.md'
W_GITHUB_URL = ''  # W... is a Wendy Test 

PATH = 'content'
PAGE_PATHS = ['page']        # Static content, appears as button on main nav bar.
ARTICLE_PATHS = ['darwin', 'stupid', 'rules']     # generated content.

TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = 'en'

# Blogroll
LINKS = (('Darwin Awards', 'https://darwinawards.com/darwin/'),
         ('Honorable Mentions', 'https://darwinawards.com/stupid/'),
         ('Rules', 'https://darwinawards.com/rules/'),
         ('Slush', 'https://darwinawards.com/slush/new'),)

# Social widget
SOCIAL = (('Substack Newsletter', 'https://darwinawards.substack.com'),
          ('Twitter Darwin', 'https://twitter.com/DarwinAwards'),
          ('Facebook Darwin', 'https://www.facebook.com/TheDarwinAwards'),
          ('Homepage Darwin', 'https://darwinawards.com'),)

THEME_TEMPLATES_OVERRIDES = ['theme/notmyidea/templates']  # works for base.html index.html override.
### August 2022 -- STATIC WRONGLY SOURCES FROM ./venv/pelican/lib/python3.8/site-packages/pelican/themes/notmyidea/static/css/main.css
### Failed to source these static files from the local themes directory,
### tried many combinations of settings and paths.
### Currently the best idea I have, is to uncomment static_excludes and
### Ref: https://docs.getpelican.com/en/stable/settings.html
### Ref: https://stackoverflow.com/questions/61040131/why-does-pelican-ignore-static-paths
THEME_STATIC_PATHS = ['theme/notmyidea/static']           # does NOT seem to source css...
# STATIC_EXCLUDES = ['./venv/pelican/lib/python3.8/site-packages/pelican/themes/notmyidea/static/css/main.css']

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

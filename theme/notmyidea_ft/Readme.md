## A pelican theme based on 'notmyidea'

### https://codeberg.org/F_Thoma/NotMyIdea-Theme-Pelican/src/branch/master

This is a theme for the static site generator [pelican](https://github.com/getpelican/pelican).
It's based on the theme 'notmyidea' which is [included in pelican](https://github.com/getpelican/pelican/tree/master/pelican/themes/notmyidea).

The initial commit already has the social media icons removed since their copyright is not entirely sorted out: https://github.com/getpelican/pelican/issues/2179

### Using this theme
Download the folder `notmyidea`.
Run pelican with the argument `-t /path/to/notmyidea` or put the line `THEME = '/path/to/notmyidea'` into the `pelicanconf.py` file.
Take a look at the `pelicanconf.py` provided in this repo to configure theme-specific features.

Add the tag `ArticlePic: images/picture.png` to your article or page to show wide pictures at the top of the page between the navigation bar and the beginning of the article/page. 

### Features
- mobile friendly (but not highly optimized)
- logo and favicon possible
- easy to change colors
- comes with a dark theme (setting can optionally be saved to local storage)
- supports the plugin [`simple-footnotes`](https://github.com/pelican-plugins/simple-footnotes/)
- light bot protection for emails addresses (they can be encrypted so that bots which don't use javascript won't get the email address)
- Optionally show a picture above the article/page title (there can be a default and the picture can be overwritten/removed individually per page).

## License and Copyright

The Font `Roboto` is licensed under the [Apache License, Version 2.0](./notmyidea/static/fonts/Apache-LICENSE-2.0.txt). [Source](https://github.com/googlefonts/roboto).

The Font `Yanone Kaffeesatz` is licensed under the [SIL Open Font License, Version 1.1](./notmyidea/static/fonts/Yanone_Kaffeesatz-License-OFL.txt) copyrighted by The Yanone Kaffeesatz Project Authors. [Source](https://github.com/alexeiva/yanone-kaffeesatz).

The rest of this repository is under the [GNU AFFERO GENERAL PUBLIC LICENSE Version 3](LICENSE).
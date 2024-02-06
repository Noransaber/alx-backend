#!/usr/bin/env python3
'''Task 2: Get locale from request
'''

from flask import Flask, request
from flask_babel import Babel, _, lazy_gettext as lgettext

app = Flask(__name__)
app.config['LANGUAGES'] = ['en', 'es']

babel = Babel(app, locale_selector=get_locale)

def get_locale():
    """
    Get the best match with our supported languages
    """
    supported_languages = app.config['LANGUAGES']
    languages = [lang for lang in request.accept_languages if lang in supported_languages]
    if languages:
        return languages[0]
    else:
        return request.accept_languages.best_match(supported_languages)

@app.route('/')
def index():
    return _(lgettext('Welcome to our website!'))


if __name__ == "__main__":
    app.run()

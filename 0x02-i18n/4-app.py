#!/usr/bin/env python3
"""
Flask app using Babel with support for locale URL parameter.
"""

from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _


class Config:
    """
    Configuration class for Babel and supported languages.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Determines the best match for supported languages.
    Checks for 'locale' in request args first.
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """
    Root route that renders the localized index page.
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run()

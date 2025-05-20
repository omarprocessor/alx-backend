#!/usr/bin/env python3
"""
Flask app using Babel for i18n with parametrized templates.
"""

from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _


class Config:
    """
    Configuration class for supported languages and defaults.
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
    Selects the best match for the user's preferred language.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """
    Root route that renders the index page.
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run()

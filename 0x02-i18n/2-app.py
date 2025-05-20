#!/usr/bin/env python3
"""
Flask app with Babel and locale selector to determine the best match.
"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """
    Configuration for Babel supported languages and defaults.
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
    Determines the best match for supported languages
    using the request's Accept-Language header.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """
    Route handler for the root URL.
    Renders the index page.
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run()

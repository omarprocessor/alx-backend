#!/usr/bin/env python3
"""
Flask application with Babel internationalization support.
"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """
    Configuration class for Flask and Babel.
    Defines available languages, default locale, and timezone.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index() -> str:
    """
    Route handler for the root URL.
    Returns the rendered index HTML template.
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()

#!/usr/bin/env python3
'''Task 5: User login mock with forced locale support
'''

from typing import Dict, Union
from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    '''Application configuration for Babel and supported languages'''
    DEBUG = True
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """Fetch user dictionary based on 'login_as' query parameter."""
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None


@app.before_request
def before_request() -> None:
    """Executed before each requestto set the usern Flask's global context."""
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """Determine the best match locale for the request.

    Returns:
        str: Locale string (e.g., 'en' or 'fr')
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """Render the main page with appropriate translation."""
    return render_template("5-index.html")

# To test Babel without @babel.localeselector, use the line below:
# babel.init_app(app, locale_selector=get_locale)


if __name__ == "__main__":
    app.run()

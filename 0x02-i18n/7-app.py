#!/usr/bin/env python3
'''Task 7: Infer appropriate time zone'''

from flask import Flask, render_template, request, g
from flask_babel import Babel, _
from typing import Union, Dict
import pytz
from pytz.exceptions import UnknownTimeZoneError


class Config:
    '''App configuration'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """Retrieves a user dictionary based on login_as URL parameter"""
    try:
        user_id = int(request.args.get('login_as'))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None


@app.before_request
def before_request():
    """Executed before every request to set global user"""
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """Determines the best match locale"""
    url_locale = request.args.get('locale')
    if url_locale in app.config['LANGUAGES']:
        return url_locale

    if g.get('user'):
        user_locale = g.user.get('locale')
        if user_locale in app.config['LANGUAGES']:
            return user_locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    """Determines the appropriate timezone"""
    tz_param = request.args.get('timezone')
    if tz_param:
        try:
            return str(pytz.timezone(tz_param))
        except UnknownTimeZoneError:
            pass

    if g.get('user'):
        tz_user = g.user.get('timezone')
        try:
            return str(pytz.timezone(tz_user))
        except (UnknownTimeZoneError, TypeError):
            pass

    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/')
def index():
    """Main route handler"""
    return render_template('7-index.html')


if __name__ == "__main__":
    app.run()

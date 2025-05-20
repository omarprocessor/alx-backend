#!/usr/bin/env python3
"""Flask app with user login simulation and localization"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext as _
from typing import Optional, Dict


class Config:
    """Flask configuration class for Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


users: Dict[int, Dict[str, Optional[str]]] = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Optional[Dict]:
    """Returns a user dictionary based on login_as URL parameter"""
    try:
        user_id = int(request.args.get('login_as'))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None


@app.before_request
def before_request() -> None:
    """Set user before handling the request"""
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """Select best match language"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """Render homepage"""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()

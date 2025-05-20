#!/usr/bin/env python3
"""
Basic Flask application that renders a welcome message
at the root route using a template.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index() -> str:
    """
    Route handler for the root URL.
    Returns the rendered index HTML template.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()

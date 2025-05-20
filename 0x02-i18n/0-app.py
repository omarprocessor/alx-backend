from flask import Flask, render_template
"""
This module renders index.html which contains h1 'Hello World'
"""


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)

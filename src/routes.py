from flask import render_template
from . import app


@app.route('/')
def home():
    """Home route."""
    return render_template('home.html', title='welcome!')

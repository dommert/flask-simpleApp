# Flask-simpleApp 
# Version 1.0-alpha
# (C) 2018 - Abstergo Inc

from flask import request
from flask_simpleApp import app


@app.route('/')
def hello_world_route():
    return 'Hello, World!'

@app.route('/about')
def about_route():
    if request.args.get("var") is None:
        testVar = 'Unknown'
    else:
        testVar= request.args.get("var")
    data = 'About Me '+testVar
    return data

# Catch All
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'You want path: %s' % path
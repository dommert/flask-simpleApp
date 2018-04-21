# Flask-simpleApp 
# Version 1.0-alpha
# (C) 2018 - Abstergo Inc

from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('app.cfg')


from flask_simpleApp.routes import *

if __name__ == '__main__':
    app.run(host='localhost', port=5001, debug=True)


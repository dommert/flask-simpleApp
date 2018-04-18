# Flask-simpleApp 
# Version 1.0-alpha
# (C) 2018 - Abstergo Inc

from flask_sqlalchemy import SQLAlchemy
from flask_simpleApp import app

dbfile = 'note.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+dbfile
db = SQLAlchemy(app)


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(120), unique=True, nullable=False)
    content = db.Column(db.Text, nullable=False)
    title = db.Column(db.String(120))

    def __repr__(self):
        return '<ID %r : Slug %r>' % (self.id, self.slug)
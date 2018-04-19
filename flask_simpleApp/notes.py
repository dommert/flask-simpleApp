# Flask-simpleApp
# Version 1.0-alpha
# (C) 2018 - Abstergo Inc

from flask_simpleApp.model import db, Note


# Create Databases
def createDB():
    db.create_all()
    return 'DB Created! (hopefully) '

# New Note
def newNote(slug, content, title=None):
    note = Note(slug=slug, content=content, title=title)
    db.session.add(note)
    db.session.commit()
    db.session.close()
    return "Note Created (maybe)"

# Remove Note
def removeNote(nid):
    note = Note.query.get(nid)
    db.session.delete(note)
    db.session.commit()
    db.session.close()
    return "Removed "

# List Note/s
def listNote():
    note = Note.query.all()
    return note

# Read Note
def readNote(nid):
    note = Note.query.get(nid)
    return note

# Update Note
def updateNote(nid, noteData):
    note = Note.query.get(nid)
    # Update Note Data
    note.title = noteData.title
    note.slug = noteData.slug
    note.content = noteData.content
    # Commit
    db.session.add(note)
    db.session.commit()
    db.session.close()
    return 'Note Updated '
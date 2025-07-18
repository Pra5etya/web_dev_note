from . import db
from .config import config_models
from sqlalchemy.dialects.postgresql import UUID
import uuid


'''
File ini berisi pembuatan database dan pembuatan table
'''


# db creation
# ========================
def create_db(): 
    config_models()

# table creation
# ========================
class Author(db.Model):
    id = db.Column(UUID(as_uuid = True), primary_key = True, default = uuid.uuid4, unique = True, nullable = False)
    name = db.Column(db.String(50), nullable = False)
    books = db.relationship('Book', backref = 'author', lazy = True)

    def __repr__(self):
        return f'<Author {self.name}>'

class Book(db.Model):
    id = db.Column(UUID(as_uuid = True), primary_key = True, default = uuid.uuid4, unique = True, nullable = False)
    title = db.Column(db.String(50), nullable = False)
    author_id = db.Column(UUID(as_uuid = True), db.ForeignKey('author.id'), nullable = False)

    def __repr__(self):
        return f'<Book {self.title}>'

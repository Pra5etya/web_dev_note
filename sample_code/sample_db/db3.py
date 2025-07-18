from web_dev import db
from .models import Author, Book


'''
File ini berisi query ke database
'''


# Author Table
# ======================
def insert_tb_author(ct_name): 
    insert_author = Author(name = ct_name)

    db.session.add(insert_author)
    db.session.commit()
    db.session.close()

def read_tb_author(): 
    return Author.query.all()

def edit_tb_author(ct_data, form_data): 
    ct_data.name = form_data.get('name', ct_data.name)
    db.session.commit()
    db.session.close()

def delete_tb_author(ct_data): 
    db.session.delete(ct_data)
    db.session.commit()
    db.session.close()

# Book Table
# ======================
def insert_tb_book(ct_title, ct_author): 
    insert_book = Book(title = ct_title, author_id = ct_author)

    db.session.add(insert_book)
    db.session.commit()
    db.session.close()

def read_tb_book(): 
    Book.query.all()

def edit_tb_book(ct_data, form_data): 
    ct_data.title = form_data.get('title', ct_data.title)
    ct_data.author_id = form_data.get('author_id', ct_data.author_id)

    db.session.commit()
    db.session.close()

def delete_tb_book(ct_data): 
    db.session.delete(ct_data)
    db.session.commit()
    db.session.close()
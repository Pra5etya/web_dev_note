from . import app, db
from .models import Author, Book
from flask import render_template, url_for, flash, redirect, request
import uuid
from .controller import (
    insert_tb_author, 
    read_tb_author, 
    edit_tb_author, 
    delete_tb_author, 
    insert_tb_book, 
    read_tb_book, 
    edit_tb_book, 
    delete_tb_book
    )


'''
File ini berisi routes dari web agar bisa di proses ke database
'''



# author views
# ========================

@app.route('/')
def index():
    authors = read_tb_author()
    return render_template('index.html', authors = authors)

@app.route('/author/new', methods = ['GET', 'POST'])
def new_author():
    if request.method == 'POST':
        # form data
        name_str = request.form['name']

        insert_tb_author(ct_name = name_str)

        flash('Author has been created!', 'success')
        return redirect(url_for('index'))
    return render_template('new_author.html')

@app.route('/author/<uuid:author_id>')
def author_detail(author_id):
    author = Author.query.get_or_404(author_id)
    return render_template('author_detail.html', author = author)

@app.route('/author/<uuid:author_id>/delete', methods=['POST'])
def delete_author(author_id):
    author = Author.query.get_or_404(author_id)

    delete_tb_author(ct_data = author)

    flash('Author has been deleted!', 'success')
    return redirect(url_for('index'))

# book views
# ========================

@app.route('/book/new', methods = ['GET', 'POST'])
def new_book():
    if request.method == 'POST':
        title_str = request.form['title']
        author_id_str = request.form['author_id']

        try:
            # Convert author_id string to UUID object
            author_id = uuid.UUID(author_id_str)

        except ValueError:
            flash('Invalid Author ID format', 'danger')
            return redirect(url_for('new_book'))

        insert_tb_book(ct_title = title_str, ct_author = author_id)

        flash('Book has been created!', 'success')
        return redirect(url_for('index'))
    
    authors = read_tb_book()
    return render_template('new_book.html', authors = authors)

@app.route('/book/<uuid:book_id>')
def book_detail(book_id):
    book = Book.query.get_or_404(book_id)
    return render_template('book_detail.html', book = book)


@app.route('/book/<uuid:book_id>/delete', methods = ['POST'])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)

    delete_tb_book(ct_data = book)

    flash('Book has been deleted!', 'success')
    return redirect(url_for('index'))
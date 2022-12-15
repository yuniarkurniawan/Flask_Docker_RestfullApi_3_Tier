from flask import request, jsonify, make_response
from collections import OrderedDict
from models import Book, Author
from sqlalchemy import text, String, func
from utils import format_local_datetime
from database import db
from datetime import datetime


# ================= BEGIN AUTHOR SERVICE
def update_author_service(id, data):
    try:
        dict_json_response = OrderedDict()
        author = Author.query.get(id)
        if author:
            if request.method == 'PUT':
                author.author_name = data['author_name']
                author.address = data['address']
                author.description = data['description']
            else:
                if data.get('author_name'):
                    author.author_name = data['author_name']
                if data.get('address'):
                    author.author_name = data['address']
                if data.get('description'):
                    author.author_name = data['description']

            author.updated_date = datetime.now()
            db.session.commit()
            dict_author = OrderedDict()
            dict_author['id'] = author.id
            dict_author['author_name'] = author.author_name
            dict_author['address'] = author.address
            dict_author['description'] = author.description

            dict_json_response = OrderedDict()
            dict_json_response['data'] = dict_author
            dict_json_response['message'] = 'success'
            dict_json_response['code'] = 200
            return make_response(jsonify(dict_json_response), 20)
        else:
            dict_json_response['message'] = 'Data not found'
            dict_json_response['code'] = 200
            return make_response(jsonify(dict_json_response), 200)
    except Exception as e:
        dict_json_response = OrderedDict()
        dict_json_response['message'] = e
        dict_json_response['code'] = 400
        return make_response(jsonify(dict_json_response), 400)


def delete_author_service(id):
    try:
        dict_json_response = OrderedDict()
        author = Author.query.get(id)
        if author:
            db.session.delete(author)
            db.session.commit()
            dict_json_response['message'] = 'success'
            dict_json_response['code'] = 200
            return make_response(jsonify(dict_json_response), 200)
        else:
            dict_json_response['message'] = 'Data not found'
            dict_json_response['code'] = 200
            return make_response(jsonify(dict_json_response), 200)
    except Exception as e:
        dict_json_response = OrderedDict()
        dict_json_response['message'] = e
        dict_json_response['code'] = 400
        return make_response(jsonify(dict_json_response), 400)


def add_author_service(data):
    try:
        author_name = data['author_name']
        address = data['address']
        description = data['description']
        author = Author(author_name=author_name,
                        address=address,
                        description=description,
                        books=[])
        db.session.add(author)
        db.session.commit()

        dict_author = OrderedDict()
        dict_author['id'] = author.id
        dict_author['author_name'] = author.author_name
        dict_author['address'] = author.address
        dict_author['description'] = author.description
        dict_author['created_date'] = \
            format_local_datetime(author.created_date)

        dict_json_response = OrderedDict()
        dict_json_response['data'] = dict_author
        dict_json_response['message'] = 'success'
        dict_json_response['code'] = 201

        return make_response(jsonify(dict_json_response), 201)

    except Exception as e:
        dict_json_response = OrderedDict()
        dict_json_response['message'] = e
        dict_json_response['code'] = 400
        return make_response(jsonify(dict_json_response), 400)


def list_author_service(page, per_page, search):

    try:
        fetch_author = Author.query.filter(
                func.lower(Author.author_name).like('%'+search+'%')
                | func.lower(Author.address).like('%'+search+'%')
                | func.lower(Author.description).like('%'+search+'%'))\
            .order_by(Author.id.asc())\
            .paginate(page=page, per_page=per_page)

        list_data_author = []
        for data in fetch_author:
            dict_author = OrderedDict()
            dict_author['id'] = data.id
            dict_author['author_name'] = data.author_name
            dict_author['address'] = data.address
            dict_author['description'] = data.description
            dict_author['created_date'] = \
                format_local_datetime(data.created_date)
            list_data_author.append(dict_author)

        pagination = {
            "page": fetch_author.page,
            'pages': fetch_author.pages,
            'total_count': fetch_author.total,
            'prev_page': fetch_author.prev_num,
            'next_page': fetch_author.next_num,
            'has_next': fetch_author.has_next,
            'has_prev': fetch_author.has_prev,
        }

        dict_json_response = OrderedDict()
        dict_json_response['data'] = list_data_author
        dict_json_response['pagination'] = pagination
        dict_json_response['message'] = 'success'
        dict_json_response['code'] = 200

        return make_response(jsonify(dict_json_response), 200)

    except Exception as e:
        dict_json_response = OrderedDict()
        dict_json_response['message'] = e
        dict_json_response['code'] = 400
        return make_response(jsonify(dict_json_response), 400)

# =========================== END AUTHOR API ===========================


# ================= BEGIN BOOK SERVICE
def update_book_service(id, data):
    try:
        dict_json_response = OrderedDict()
        book = Book.query.get(id)
        if book:
            if request.method == 'PUT':
                book.title = str(data['title']).title()
                book.year = int(data['year'])
                book.author_id = int(data['author_id'])
                book.description = data['description']
            else:
                if data.get('title'):
                    book.title = str(data['title']).title()
                if data.get('author_id'):
                    book.author_id = data['author_id']
                if data.get('year'):
                    book.author_name = int(data['year'])
                if data.get('description'):
                    book.description = data['description']

            book.updated_date = datetime.now()
            db.session.commit()
            dict_book = OrderedDict()
            dict_book['id'] = book.id
            dict_book['title'] = book.title
            dict_book['author_name'] = book.author.author_name
            dict_book['year'] = book.year
            dict_book['description'] = book.description
            dict_book['updated_date'] = \
                format_local_datetime(book.updated_date)

            dict_json_response['data'] = dict_book
            dict_json_response['message'] = 'success'
            dict_json_response['code'] = 200
            return make_response(jsonify(dict_json_response), 20)
        else:
            dict_json_response['message'] = 'Book not found'
            dict_json_response['code'] = 200
            return make_response(jsonify(dict_json_response), 200)
    except Exception as e:
        dict_json_response = OrderedDict()
        dict_json_response['message'] = e
        dict_json_response['code'] = 400
        return make_response(jsonify(dict_json_response), 400)


def delete_book_service(id):
    try:
        dict_json_response = OrderedDict()
        book = Book.query.get(id)
        if book:
            db.session.delete(book)
            db.session.commit()
            dict_json_response['message'] = 'success'
            dict_json_response['code'] = 200
            return make_response(jsonify(dict_json_response), 200)
        else:
            dict_json_response['message'] = 'Book not found'
            dict_json_response['code'] = 200
            return make_response(jsonify(dict_json_response), 200)
    except Exception as e:
        dict_json_response = OrderedDict()
        dict_json_response['message'] = e
        dict_json_response['code'] = 400
        return make_response(jsonify(dict_json_response), 400)


def list_book_service(page, per_page, search):
    try:

        fetch_book = Book.query.join(Author).filter(
                func.cast(Book.year, String).like('%'+search+'%')
                | func.lower(Book.title).like('%'+search+'%')
                | func.lower(Author.author_name).like('%'+search+'%')
                | func.lower(Book.description).like('%'+search+'%'))\
            .order_by(Book.id.asc())\
            .paginate(page=page, per_page=per_page)

        list_book = []
        for data in fetch_book:
            dict_book = OrderedDict()
            dict_book['id'] = data.id
            dict_book['title'] = data.title
            dict_book['author_name'] = data.author.author_name
            dict_book['year'] = data.year
            dict_book['description'] = data.description
            dict_book['created_date'] = \
                format_local_datetime(data.created_date)
            list_book.append(dict_book)

        pagination = {
            "page": fetch_book.page,
            'pages': fetch_book.pages,
            'total_count': fetch_book.total,
            'prev_page': fetch_book.prev_num,
            'next_page': fetch_book.next_num,
            'has_next': fetch_book.has_next,
            'has_prev': fetch_book.has_prev,
        }

        dict_json_response = OrderedDict()
        dict_json_response['data'] = list_book
        dict_json_response['pagination'] = pagination
        dict_json_response['message'] = 'success'
        dict_json_response['code'] = 200

        return make_response(jsonify(dict_json_response), 200)
    except Exception as e:
        dict_json_response = OrderedDict()
        dict_json_response['message'] = e
        dict_json_response['code'] = 400
        return make_response(jsonify(dict_json_response), 400)


def add_book_service(data):
    try:
        dict_json_response = OrderedDict()
        author = Author.query.get(int(data['author_id']))
        if author:
            book = Book(title=str(data['title']).title(),
                        year=int(data['year']), author_id=author.id,
                        description=data['description'])
            db.session.add(book)
            db.session.commit()

            dict_book = OrderedDict()
            dict_book['id'] = book.id
            dict_book['title'] = book.title
            dict_book['year'] = book.year
            dict_book['author'] = book.author.author_name
            dict_book['created_date'] = \
                format_local_datetime(book.created_date)

            dict_json_response = OrderedDict()
            dict_json_response['data'] = dict_book
            dict_json_response['message'] = 'success'
            dict_json_response['code'] = 201
            return make_response(jsonify(dict_json_response), 201)
        else:
            dict_json_response['message'] = 'Author not found'
            dict_json_response['code'] = 200
            return make_response(jsonify(dict_json_response), 200)
    except Exception as e:
        dict_json_response = OrderedDict()
        dict_json_response['message'] = e
        dict_json_response['code'] = 400
        return make_response(jsonify(dict_json_response), 400)

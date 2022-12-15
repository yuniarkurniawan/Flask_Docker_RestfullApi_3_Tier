from flask import Blueprint, request
from services import update_book_service, delete_book_service, \
    list_book_service, add_book_service, update_author_service, \
    delete_author_service, add_author_service, list_author_service


author_routes = Blueprint('author_routes', __name__)
book_routes = Blueprint("book_routes", __name__)


# ============== AUTHOR BOOK ROUTES
@author_routes.route('/list_author', methods=['GET'])
def get_author_list():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 5, type=int)
    search = request.args.get('search', type=str)
    return list_author_service(page, per_page, search)


@author_routes.route('/add_author', methods=['POST'])
def add_author():
    data = request.get_json()
    return add_author_service(data)


@author_routes.route('/update_author/<int:id>', methods=['PUT', 'PATCH'])
def update_author(id):
    data = request.get_json()
    return update_author_service(id, data)


@author_routes.route('/delete_author/<int:id>', methods=['DELETE'])
def delete_author(id):
    return delete_author_service(id)


# ============== BEGIN BOOK ROUTES

@book_routes.route('/list_book', methods=['GET'])
def get_book_lists():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 5, type=int)
    search = request.args.get('search', type=str)
    return list_book_service(page, per_page, search)


@book_routes.route('/add_book', methods=['POST'])
def add_book():
    data = request.get_json()
    return add_book_service(data)


@book_routes.route('/delete_book/<int:id>', methods=['DELETE'])
def delete_book(id):
    return delete_book_service(id)


@book_routes.route('/update_book/<int:id>', methods=['PUT', 'PATCH'])
def update_book(id):
    data = request.get_json()
    return update_book_service(id, data)

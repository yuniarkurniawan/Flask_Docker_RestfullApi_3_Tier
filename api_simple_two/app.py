from flask import Flask
from routes import author_routes, book_routes
from database import db


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///author_book.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_SORT_KEYS'] = False


db.init_app(app)
with app.app_context():
    db.create_all()

app.register_blueprint(author_routes, url_prefix='/api/v1/author')
app.register_blueprint(book_routes, url_prefix='/api/v1/book')

if __name__ == '__main__':
    app.run(debug=True)

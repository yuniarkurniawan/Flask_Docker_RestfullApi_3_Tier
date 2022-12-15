from database import db


class Author(db.Model):

    __tablename__ = 'author'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author_name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.Text, nullable=False)
    created_date = db.Column(db.DateTime, server_default=db.func.now())
    updated_date = db.Column(db.DateTime, server_default=db.func.now())
    description = db.Column(db.Text)
    books = db.relationship('Book',
                            backref='Author',
                            cascade='all,delete-orphan')

    def __init__(self, **kwargs):
        self.author_name = kwargs['author_name']
        self.address = kwargs['address']
        self.description = kwargs['description']
        self.books = kwargs['books']


class Book(db.Model):

    __tablename__ = 'book'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    author = db.relationship("Author",)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    created_date = db.Column(db.DateTime, server_default=db.func.now())
    updated_date = db.Column(db.DateTime, server_default=db.func.now())
    description = db.Column(db.Text)

    def __init__(self, **kwargs):
        self.title = kwargs['title']
        self.year = int(kwargs['year'])
        self.author_id = kwargs['author_id']
        self.description = kwargs['description']

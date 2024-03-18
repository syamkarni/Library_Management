from .database import db
from flask_security import UserMixin, RoleMixin
import datetime

class Role(db.Model, RoleMixin):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    users = db.relationship('UserRole', backref='role')

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    u_mail = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    fs_uniquifier = db.Column(db.String(300), unique=True, nullable=False)
    roles = db.relationship('UserRole', backref='user')
    active = db.Column(db.Boolean)
    book_requests = db.relationship('BookRequest', backref='user', lazy='dynamic')

    def __init__(self, u_mail, password, fs_uniquifier):
        self.u_mail = u_mail
        self.password = password
        self.fs_uniquifier = fs_uniquifier

class UserRole(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))

class Book(db.Model):
    __tablename__ = "book"
    book_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    book_name = db.Column(db.String(50))
    book_author = db.Column(db.String(50))
    pages_in_book = db.Column(db.Integer)
    price = db.Column(db.Integer)
    content = db.Column(db.Text)
    section_id = db.Column(db.Integer, db.ForeignKey('section.id'))
    section = db.relationship('Section', backref='books')

class Section(db.Model):
    __tablename__ = 'section'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(250))
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())

class BookRequest(db.Model):
    __tablename__ = 'book_request'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    book_id = db.Column(db.Integer, db.ForeignKey('book.book_id'))
    date_requested = db.Column(db.DateTime, default=db.func.current_timestamp())
    status = db.Column(db.String(20), default='requested')  # e.g., requested, approved, declined

    book = db.relationship('Book', backref='requests')

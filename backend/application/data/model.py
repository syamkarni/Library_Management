from .database import db
from flask_security import UserMixin, RoleMixin



class Role(db.Model, RoleMixin):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    users = db.relationship('UserRole', back_populates='role')

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    u_mail = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    fs_uniquifier = db.Column(db.String(300), unique=True, nullable=False)
    roles = db.relationship('UserRole', back_populates='user')
    active = db.Column(db.Boolean)
    borrowed_books = db.relationship('Book', back_populates='borrower', overlaps="borrower")
    assigned_books = db.relationship('Book', back_populates='librarian', overlaps="librarian")


    def __init__(self, u_mail, password, fs_uniquifier):
        self.u_mail = u_mail
        self.password = password
        self.fs_uniquifier = fs_uniquifier

class UserRole(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    user = db.relationship('User', back_populates='roles')
    role = db.relationship('Role', back_populates='users')






class Book(db.Model):
    __tablename__ = "book"
    book_id = db.Column(db.Integer, primary_key = True, autoincrement= True)
    book_name = db.Column(db.String(50))
    book_author = db.Column(db.String(50))
    pages_in_book = db.Column(db.Integer)
    price = db.Column(db.Integer)
    date_issued = db.Column(db.DateTime)
    date_returned = db.Column(db.DateTime)
    content = db.Column(db.Text)
    section_id = db.Column(db.Integer, db.ForeignKey('section.id'))
    section = db.relationship('Section', back_populates='books')
    borrower_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    borrower = db.relationship('User', back_populates='borrowed_books', overlaps="borrowed_books")
    librarian_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    librarian = db.relationship('User', back_populates='assigned_books', overlaps="assigned_books")
    

class Section(db.Model):
    __tablename__ = 'section'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    description = db.Column(db.String(250))
    books = db.relationship('Book', back_populates='section')

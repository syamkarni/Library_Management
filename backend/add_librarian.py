from main import app
from application.data.model import db, User, Role, UserRole
from werkzeug.security import generate_password_hash
import secrets

with app.app_context():
    if User.query.filter_by(u_mail="librarian@a.com").first() is None:
        fs_uniquifier = secrets.token_hex(16)
        librarian_user = User(
            u_mail="librarian@a.com",
            password=generate_password_hash("your_password"),
            fs_uniquifier=fs_uniquifier,
        )
        db.session.add(librarian_user)
        librarian_role = Role.query.filter_by(name="librarian").first()
        if librarian_role:
            user_role = UserRole(user=librarian_user, role=librarian_role)
            db.session.add(user_role)

        db.session.commit()
        print("Librarian user added successfully.")
    else:
        print("Librarian user already exists.")

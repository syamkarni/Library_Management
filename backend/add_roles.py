from main import app  # Import the Flask app instance created in main.py
from application.data.model import db, Role

with app.app_context():
    # Check and add 'user' role
    if Role.query.filter_by(name="user").first() is None:
        user_role = Role(name="user")
        db.session.add(user_role)

    # Check and add 'admin' role
    if Role.query.filter_by(name="admin").first() is None:
        admin_role = Role(name="admin")
        db.session.add(admin_role)

    # Commit changes to the database
    db.session.commit()

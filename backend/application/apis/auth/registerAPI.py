from flask import jsonify
import secrets
from werkzeug.security import generate_password_hash
from flask_restful import Resource, reqparse
from application.data.model import db, User, Role, UserRole

user_post_args = reqparse.RequestParser()
user_post_args.add_argument('u_mail', type=str, required=True, help="User email is required !!")
user_post_args.add_argument('password', type=str, required=True, help="Password is required to register.")
user_post_args.add_argument('role', type=str, required=True, help="Role is required to register.")

class RegisterAPI(Resource):
    def post(resource):
        args = user_post_args.parse_args()
        u_mail = args.get('u_mail')
        password = args.get('password')
        role_name = args.get('role')

        print(f"Attempting to register: Email - {u_mail}, Role - {role_name}")

        user = User.query.filter_by(u_mail=u_mail).first()
        if user:
            return jsonify({'status': 'failed', 'message': 'This Email is already Registered'})

        hashed_password = generate_password_hash(password)
        fs_uniquifier = secrets.token_hex(16)

        new_user = User(u_mail=u_mail, password=hashed_password, fs_uniquifier=fs_uniquifier)
        db.session.add(new_user)

        role = Role.query.filter_by(name=role_name).first()
        if not role:
            return jsonify({'status': 'failed', 'message': 'Role not found'})

        new_user_role = UserRole(user_id=new_user.user_id, role_id=role.id)
        db.session.add(new_user_role)
        db.session.commit()

        print(f"User {u_mail} successfully registered with role {role_name}")
        return jsonify({'status': 'success', 'message': "User is Successfully registered."})

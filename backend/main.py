# Importing essential libraies--------------------------------
import os
import secrets
from flask import Flask, current_app, jsonify, request, abort
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_restful import Resource, Api
from flask_cors import CORS
from werkzeug.security import generate_password_hash
from celery.schedules import crontab
from werkzeug.security import generate_password_hash

from application.data.database import db
from application.data.model import *
from application.security import security, user_datastore
import application.config as config


from application.apis.book.bookApi import AllBookAPI
from application.apis.book.bookApi import BookAPI
from application.apis.auth.loginAPI import LoginAPI
from application.apis.auth.loginAPI import RefreshTokenAPI
from application.apis.auth.registerAPI import RegisterAPI
from application.apis.section.sectionapi import AllSectionAPI
from application.apis.section.sectionapi import SectionAPI   



app = Flask(__name__, template_folder= "./templates")
app.config.from_object(config)
app.app_context().push()
migrate = Migrate(app, db)


#  Flask CORS
CORS(app, supports_credentials=True)

# Add CORS headers to every response
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET, PUT, POST, DELETE, OPTIONS'

    return response

@app.after_request
def after_request(response):
    response = add_cors_headers(response)
    return response




db.init_app(app)

api = Api(app)
api.init_app(app)


JWTManager(app)


security.init_app(app, user_datastore)

api.add_resource(AllBookAPI, "/api/book")
api.add_resource(BookAPI, "/api/book/<int:book_id>")

api.add_resource(AllSectionAPI, '/api/sections')
api.add_resource(SectionAPI, '/api/sections/<int:section_id>')

api.add_resource(RegisterAPI, "/api/register")
api.add_resource(LoginAPI,'/api/login')

api.add_resource(RefreshTokenAPI,"/api/refresh_token")

# def new_librarian():
@app.route('/api/sections/<int:section_id>', methods=['PUT'])
def update_section(section_id):
    section = Section.query.get(section_id)
    if not section:
        abort(404, "Section not found")
    
    data = request.json
    section.name = data.get('name', section.name)
    section.description = data.get('description', section.description)
    # Update other fields as necessary

    db.session.commit()
    return jsonify({"message": "Section updated successfully"})


with app.app_context():
    db.create_all()
    # new_librarian()
# testing code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)
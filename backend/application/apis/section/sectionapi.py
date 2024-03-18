from flask_restful import Resource, reqparse, fields, marshal_with
from application.data.model import db, Section
from flask import jsonify, current_app

# Argument parsers
section_post_args = reqparse.RequestParser()
section_post_args.add_argument('name', type=str, required=True, help="Name required")
section_post_args.add_argument('description', type=str)
section_post_args.add_argument('date_created', type=str, required=True, help="Creation date required")

section_put_args = reqparse.RequestParser()
section_put_args.add_argument('name', type=str)
section_put_args.add_argument('description', type=str)
section_put_args.add_argument('date_created', type=str)

# Resource fields
section_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'description': fields.String,
    'date_created': fields.String
}

# Resource classes
class AllSectionAPI(Resource):
    @marshal_with(section_fields)
    def get(self):
        sections = Section.query.all()
        return sections

    @marshal_with(section_fields)
    def post(self):
        try:
            args = section_post_args.parse_args()
            section = Section(name=args['name'], description=args['description'], date_created=args['date_created'])
            db.session.add(section)
            db.session.commit()
            return section, 201
        except Exception as e:
            # Log the exception
            current_app.logger.error(f"Error adding section: {e}")
            return jsonify(error=str(e)), 500
        
    

class SectionAPI(Resource):
    @marshal_with(section_fields)
    def get(self, section_id):
        section = Section.query.filter_by(id=section_id).first()
        if not section:
            return {'message': 'Section not found'}, 404
        return section

    @marshal_with(section_fields)
    def put(self, section_id):
        args = section_put_args.parse_args()
        section = Section.query.filter_by(id=section_id).first()
        if not section:
            return {'message': 'Section not found'}, 404

        if args['name']:
            section.name = args['name']
        if args['description']:
            section.description = args['description']
        if args['date_created']:
            section.date_created = args['date_created']
        db.session.commit()
        return section

    def delete(self, section_id):
        section = Section.query.filter_by(id=section_id).first()
        if not section:
            return {'message': 'Section not found'}, 404
        db.session.delete(section)
        db.session.commit()
        return {'message': 'Section deleted'}, 200

from flask import request
from flask_restful import Resource
from Model import db, Category, CategorySchema

categories_schema = CategorySchema(many=True)
category_schema = CategorySchema()

class CategoryResource(Resource):
    # GET Method for category endpoint
    def get(self):
        # Display all categories
        categories = Category.query.all()
        categories = categories_schema.dump(categories).data
        # return data and HTTP 200 status code
        return {'status': 'success', 'data': categories}, 200
    # POST Method for creating a category
    def post(self):
        # Check for JSON input data
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400

        # Validate and deserialize input
        data, errors = category_schema.load(json_data)
        if errors:
            return errors, 422

        # Check if category already exists
        category = Category.query.filter_by(name=data['name']).first()
        if category:
            return {'message': 'Category already exists'}, 400
        category = Category(
            name=json_data['name']
        )

        # Add dataset and commit changes to DB
        db.session.add(category)
        db.session.commit()

        result = category_schema.dump(category).data

        # Return HTTP status code 201
        return {"status": 'success', 'data': result}, 201

    def put(self):
        # Check for input data
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400

        # Validate and deserialize input
        data, errors = category_schema.load(json_data)
        if errors:
            return errors, 422
        # Check if category already exists for updating
        category = Category.query.filter_by(id=data['id']).first()
        if not category:
            return {'message': 'Category does not exist'}, 400
        # Update category name and commit changes to DB
        category.name = data['name']
        db.session.commit()

        result = category_schema.dump(category).data

        # Return HTTP status code 204
        return {"status": 'success', 'data': result}, 204

    def delete(self):
        # Check for input data
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400

        # Validate and deserialize input
        data, errors = category_schema.load(json_data)
        if errors:
            return errors, 422
        category = Category.query.filter_by(id=data['id']).delete()
        db.session.commit()

        result = category_schema.dump(category).data

        # Return HTTP status code 204
        return {"status": 'success', 'data': result}, 204
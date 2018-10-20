from flask import Blueprint
from flask_restful import Api
from resources.Hello import Hello


# Blueprint which will be registered in the app
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Add Route to Hello Class
api.add_resource(Hello, '/Hello')
from flask_restful import Resource


class Hello(Resource):
    # GET Method Call
    def get(self):
        return {"message": "Hello, World!"}
    # POST Method Call
    def post(self):
        return {"message": "Hello, World!"}
from flask import Flask


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    from app import api_bp
    # Created blueprint is being registered here
    app.register_blueprint(api_bp, url_prefix='/api')

    # Import our model
    from Model import db
    db.init_app(app)

    return app


if __name__ == "__main__":
    app = create_app("config")
    app.run(debug=True)
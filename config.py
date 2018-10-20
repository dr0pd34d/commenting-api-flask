import os


basedir = os.path.abspath(os.path.dirname(__file__))
# Define SQLite Database file name
SQLALCHEMY_DATABASE_URI = "sqlite:///app.db"

# Postgresql database alternative parameters
#SQLALCHEMY_ECHO = False
#SQLALCHEMY_TRACK_MODIFICATIONS = True
#SQLALCHEMY_DATABASE_URI = "postgresql://username:password@localhost/database_name"


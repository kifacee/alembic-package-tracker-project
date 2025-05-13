import os

class Config:
    # alternatively, generate random secret key
    # SECRET_KEY = os.urandom(32)
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_DATABASE_URI = 'postgresql://packages:pass@localhost/package_tracker_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

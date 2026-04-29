import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:percy4u2@localhost:3306/school_tracker'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'dev-secret-key'

import base64
import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    SECRET_KEY = "Bl4H_BL%H-blAh"
    JSON_AS_ASCII = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    TOKEN_EXPIRE_MINUTES = 15
    TOKEN_EXPIRE_DAYS = 130

    PWD_HASH_SALT = base64.b64decode("salt")
    PWD_HASH_ITERATIONS = 100_000

    PWD_JWT_ALGO = 'HS256'


class TestingConfig(BaseConfig):
    TESTING = True
    #SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_DATABASE_URI = "postgres:///:memory:"


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_ECHO = True

    #SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(
        #os.path.dirname(BASEDIR), "project.db"
    #)

    #SQLALCHEMY_DATABASE_URI = "postgresql://admin:admin_password@localhost/cw4_db"
    SQLALCHEMY_DATABASE_URI = "postgresql://admin:admin_password@pg/app_db"
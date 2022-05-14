from flask import Flask
from flask_cors import CORS
from flask_restx import Api

from application.db_initialization import db
from application.views.favorites import favorites_ns
from application.views.authentication import auth_ns
from application.views.genres import genres_ns
from application.views.movies import movie_ns
from application.views.directors import director_ns
from application.views.users import user_ns

api = Api(authorizations={
        "Bearer": {"type": "apiKey", "in": "header", "name": "Authorization"}
    },
    title="Flask Course Project 3",
    version='1.0',
    description='API сервиса БД с фильмами. Тут должно быть длинное описание всех доступных опций АПИ? ',
    doc="/docs",
)

# Нужно для работы с фронтендом
cors = CORS()


def create_app(config_obj):
    app = Flask(__name__)
    app.config.from_object(config_obj)

    cors.init_app(app)
    db.init_app(app)
    api.init_app(app)

    # Регистрация эндпоинтов
    api.add_namespace(genres_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)
    api.add_namespace(favorites_ns)

    return app

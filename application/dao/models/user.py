from application.dao.models.base import BaseMixin
from application.dao.models.favorite import favorite_genres, favorite_movies
from application.db_initialization import db


# Создаем класс для таблиц Пользователей
class User(BaseMixin, db.Model):
    __tablename__ = 'users'

    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255))
    surname = db.Column(db.String(255))

    # Создаем связь для избранных жанров
    # favorite_genre = db.Column(db.Integer, db.ForeignKey('genres.id'))
    genres = db.relationship('Genre', secondary=favorite_genres, back_populates="users")
    movies = db.relationship('Movie', secondary=favorite_movies, back_populates="users")

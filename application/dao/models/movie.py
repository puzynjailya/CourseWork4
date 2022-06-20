from application.dao.models.base import BaseMixin
from application.dao.models.favorite import favorite_movies
from application.db_initialization import db


# Создаем класс с фильмами
class Movie(BaseMixin, db.Model):
    __tablename__ = 'movies'

    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    trailer = db.Column(db.String(255), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    # Создаем связи с жанрами
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'), nullable=False)
    genre = db.relationship('Genre', lazy=True)

    # Создаем связи с режиссерами
    director_id = db.Column(db.Integer, db.ForeignKey('directors.id'), nullable=False)
    director = db.relationship('Director', lazy=True)

    # Создаем связь с пользователями
    users = db.relationship('User', secondary=favorite_movies, back_populates="movies")

    def __repr__(self):
        return f"<Movie '{self.title.title()}'-'{self.year.title()}'>"

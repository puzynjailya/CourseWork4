from application.dao.models.base import BaseMixin
from application.db_initialization import db

# Создаем промежуточную таблицы
favorite_genres = db.Table('favorite_genres',
                           db.Column('user_id', db.ForeignKey('users.id'), primary_key=True),
                           db.Column('genre_id', db.ForeignKey('genres.id'), primary_key=True)
                           )

favorite_movies = db.Table('favorite_movies',
                           db.Column('user_id', db.ForeignKey('users.id'), primary_key=True),
                           db.Column('movie_id', db.ForeignKey('movies.id'), primary_key=True)
                           )

# Можно было сделать и так (если вдруг, в дальнейшем захотелось бы добавлять больше информации в таблицы)
'''
# Создаем промежуточную таблицы
class FavoriteGenre(BaseMixin, db.Model):
    __tablename__ = 'favorite_genres'

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'), primary_key=True)


class FavoriteMovie(BaseMixin, db.Model):
    __tablename__ = 'favorite_movies'

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'))
'''

from application.dao import DirectorDAO, GenreDAO, MovieDAO, UserDAO
from application.services.auth import AuthService
from application.services.director import DirectorService
from application.services.genre import GenreService
from application.services.movie import MovieService
from application.services.user import UserService
from application.services.favorite import FavoriteService
from application.db_initialization import db

director_dao = DirectorDAO(session=db.session)
genre_dao = GenreDAO(session=db.session)
movie_dao = MovieDAO(session=db.session)
user_dao = UserDAO(session=db.session)

director_service = DirectorService(dao=director_dao)
genre_service = GenreService(dao=genre_dao)
movie_service = MovieService(dao=movie_dao)
user_service = UserService(dao=user_dao)
auth_service = AuthService(dao=user_dao)
favorite_service = FavoriteService(dao=user_dao)

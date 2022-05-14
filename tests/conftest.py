from unittest.mock import MagicMock
import pytest

from application.dao import UserDAO
from application.dao.director import DirectorDAO
from application.dao.genre import GenreDAO
from application.dao.movie import MovieDAO
from application.dao.models import Director
from application.dao.models import Genre
from application.dao.models import Movie
from application.dao.models import User


# Фикстура для МОКирования Режиссеров
@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)

    d1 = Director(id=1, name='Тейлор Шеридан')
    d2 = Director(id=2, name='Квентин Тарантино')
    d3 = Director(id=3, name='Владимир Вайншток')

    director_dao.get_one = MagicMock(return_value=d1)
    director_dao.get_all = MagicMock(return_value=[d1, d2, d3])
    director_dao.create = MagicMock(return_value=Director(id=3))
    director_dao.delete = MagicMock(return_value=[d2, d3])
    director_dao.update = MagicMock(return_value=Director(id=3, name="Elona Musk"))

    return director_dao


# Фикстура для МОКирования жанров
@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)

    g1 = Genre(id=1, name='Комедия')
    g2 = Genre(id=2, name='Семейный')
    g3 = Genre(id=3, name='Фэнтези')

    genre_dao.get_by_id = MagicMock(return_value=g1)
    genre_dao.get_all = MagicMock(return_value=[g1, g2, g3])
    genre_dao.get_all_sorted_asc = MagicMock(return_value=[g3, g2, g1])
    genre_dao.get_all_sorted_desc = MagicMock(return_value=[g1, g2, g3])
    genre_dao.get_all_sort_and_page_asc = MagicMock(return_value=[g3, g2, g1])
    genre_dao.get_all_sort_and_page_desc = MagicMock(return_value=[g1, g2, g3])
    genre_dao.create = MagicMock(return_value=Genre(id=3))
    genre_dao.update = MagicMock(return_value=Genre(id=3, name="PyTest"))
    genre_dao.delete = MagicMock(return_value=[g2, g3])

    return genre_dao


# Фикстура для МОКирования фильмов
@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    m1 = Movie(id=1,
               title='Test1',
               description='Desc1',
               trailer='Tr1',
               year=2001,
               rating=1,
               genre_id=1,
               director_id=1)
    m2 = Movie(id=2,
               title='Test2',
               description='Desc2',
               trailer='Tr2',
               year=2002,
               rating=2,
               genre_id=2,
               director_id=2)
    m3 = Movie(id=3,
               title='Test3',
               description='Desc3',
               trailer='Tr3',
               year=2003,
               rating=3,
               genre_id=3,
               director_id=3)

    movie_dao.get_one = MagicMock(return_value=m1)
    movie_dao.get_all = MagicMock(return_value=[m1, m2, m3])
    movie_dao.create = MagicMock(return_value=Movie(id=3))
    movie_dao.update = MagicMock(return_value=Movie(id=3,
                                                    title='UPD1.1',
                                                    description='UPD1.2',
                                                    trailer='UPD1.3',
                                                    year=2022,
                                                    rating=4,
                                                    genre_id=5,
                                                    director_id=6))
    movie_dao.delete = MagicMock(return_value=[m2, m3])

    return movie_dao


@pytest.fixture()
def user_dao():
    user_dao = UserDAO(None)

    u1 = User(id=1, email='tester1@test.com', password='hello', name='tester1', surname='A')
    u2 = User(id=2, email='tester2@test.com', password='world', name='tester2', surname='B')

    user_dao.get_one_by_email = MagicMock(return_value=u1)
    user_dao.get_one_by_id = MagicMock(return_value=u2)
    user_dao.create = MagicMock(return_value={u1.email, u1.name, u1.surname})

    return user_dao

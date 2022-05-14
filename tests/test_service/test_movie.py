import pytest

from application.services.movie import MovieService


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        # Получаем необходимый нам жанр
        movie = self.movie_service.get_one(1)

        # Проверяем жанр на соответствия параметрам
        assert movie is not None
        assert movie['id'] is not None
        assert movie['id'] == 1

    def test_get_all(self):
        # Получаем список всех жанров
        movies = self.movie_service.get_all(director=None, genre=None, year=None, page=None, status=None)
        assert len(movies) > 0

    def test_create(self):
        # Задаем тестовый входной параметр
        data = {"name": "Тест"}
        # Выполняем сервис добавления
        movie = self.movie_service.create(data)

        assert movie is not None
        assert movie.id == 3

    # def test_update(self):
    #     # Задаем тестовый входной параметр
    #     m_data = {"id": 3,
    #               "title": "UPD1.1",
    #               "description": "UPD1.2",
    #               "trailer": "UPD1.3",
    #               "year": 2022,
    #               "rating": 4,
    #               "genre_id": 5,
    #               "director_id": 6}
    #
    #     # Выполняем сервис добавления
    #     movie = self.movie_service.update(m_data)
    #
    #     # Проверяем соответствие
    #     assert movie is not None
    #     assert movie['title'] == "UPD1.1"
    #     assert movie.description == "UPD1.2"
    #     assert movie.trailer == "UPD1.3"
    #     assert movie.id == 3
    #     assert movie.year == 2022
    #     assert movie.rating == 4
    #     assert movie.genre_id == 5
    #     assert movie.director_id == 6

    def test_delete(self):
        self.movie_service.delete(3)

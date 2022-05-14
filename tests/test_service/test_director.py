import pytest

from application.services.director import DirectorService


# Создаем класс для тестирования сервиса Режиссеров
class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)
        print(director)
        assert director is not None
        assert director['id'] is not None

    def test_get_all_directors(self):
        directors = self.director_service.get_all_directors(page=None, status=None)

        assert len(directors) > 0
        assert len(directors) == 3

    def test_create(self):
        data = {"name": "Elona Musk"}

        director = self.director_service.create(data)

        assert director is not None
        assert director.id == 3

    # def test_update(self):
    #     data = {"id": 3, "name": "Elona Musk"}
    #     did = data["id"]
    #     director = self.director_service.update(data, did)
    #
    #     assert director is not None
    #     assert director['name'] == "Elona Musk"
    #
    # # В целом, этот тест не нужен, т.к. он повторяет предыдущий в данном случае
    # def test_partially_update(self):
    #
    #     data = {"id": 3, "name": "Elona Musk"}
    #     director = self.director_service.update(data, data['id'])
    #
    #     assert director is not None
    #     assert director['name'] == "Elona Musk"

    def test_delete(self):
        self.director_service.delete(1)



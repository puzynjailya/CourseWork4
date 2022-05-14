import pytest
from application.services import UserService


# Создаем класс для тестирования сервиса пользователей
class TestUserService:

    # Инициализируем сервис работы с жанрами воткнув заглушку user_dao
    @pytest.fixture(autouse=True)
    def user_service(self, user_dao):
        self.user_service = UserService(dao=user_dao)

    def test_get_user_within_id(self):
        # Получаем необходимый нам жанр
        user = self.user_service.get_user(1)

        # Проверяем жанр на соответствия параметрам
        assert user is not None
        assert user['email'] == 'tester2@test.com'
        assert user['id'] == 2

    def test_create_user(self):
        pass




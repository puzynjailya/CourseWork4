from application.dao import UserDAO
from application.services.user import UserService


class FavoriteService(UserService):
    def __init__(self, dao: UserDAO):
        super().__init__(dao)
        self.dao = dao

    def add_favorite(self, token, data_object, movie_flag):
        """
        Сервис, предназначенный для добавления данных в сводную таблицу
        :param token: токен с данными о пользователе
        :param data_object: объект с данными
        :param movie_flag: Bool - флаг выбора. Если True, то добавляет избранный фильм, если нет, то добавляет избранный жанр
        :return: бу-га-гашеньку
        """
        data = self.decode_token(token)
        user = self.dao.get_one_by_email(email=data.get('email'))

        if movie_flag:
            self.dao.add_favorite_movie(user, data_object)

        else:
            self.dao.add_favorite_genre(user, data_object)

    def remove_favorite(self, token, data_object, movie_flag):
        """
       Сервис, предназначенный для удаления данных в сводной таблице
       :param token: токен с данными о пользователе
       :param data_object: объект с данными
       :param movie_flag: Bool - флаг выбора. Если True, то удаляет избранный фильм, если нет, то удаляет избранный жанр
       :return: бу-га-гашеньку
       """
        data = self.decode_token(token)
        user = self.dao.get_one_by_email(email=data.get('email'))

        if movie_flag:
            self.dao.remove_favorite_movie(user, data_object)

        else:
            self.dao.remove_favorite_genre(user, data_object)




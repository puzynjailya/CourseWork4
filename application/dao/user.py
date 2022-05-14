from application.dao.models import User, Movie, Genre


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one_by_email(self, email):
        """
        Возвращает найденного пользователя по email
        :param email: str - email пользователя
        :return: результат запроса
        """
        return self.session.query(User).filter(User.email == email).one_or_none()

    def get_one_by_id(self, user_id):
        return self.session.query(User).filter(User.id == user_id).first()

    def create(self, data):
        """
        Метод добалвения нового пользователя в БД
        :param data: входные данные
        :return: добавленную сущность
        """

        entity = User(**data)
        self.session.add(entity)
        self.session.commit()
        return [entity.email, entity.name, entity.surname]

    def data_update(self, user_data):
        """
        Обновление данных о пользователе
        :param user_data: dict - данные для изменения
        :return: user - с обновленными данными
        """
        user = self.get_one_by_id(user_data.get('id'))
        user.name = user_data.get('name')
        user.surname = user_data.get('surname')
        user.favorite_genre = user_data.get('favorite_genre')

        self.session.add(user)
        self.session.commit()

    def password_update(self, user: User):
        """
        Обновление пароля пользователя
        :param user: User - объект класса User
        :return: user - с обновленными данными
        """
        self.session.add(user)
        self.session.commit()

        return user

    def add_favorite_movie(self, user: User, movie: Movie):
        user.movies.append(movie)
        self.session.commit()

    def add_favorite_genre(self, user: User, genre: Genre):
        user.genres.append(genre)
        self.session.commit()

    def remove_favorite_movie(self, user, movie):
        user.movies.remove(movie)
        self.session.commit()

    def remove_favorite_genre(self, user, genre):
        user.genres.remove(genre)
        self.session.commit()

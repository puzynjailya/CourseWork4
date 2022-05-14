from sqlalchemy import desc
from application.constants import ITEMS_PER_PAGE

from application.dao.models import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_by_id(self, pk):
        """
        Метод получения записи из БД по id
        :param pk: int: индекс искомой записи
        :return: object: результат запроса
        """
        return self.session.query(Genre).filter(Genre.id == pk).one_or_none()

    def get_all(self):
        """
        Метод получения всех записей из БД
        :return: object: результат запроса
        """
        return self.session.query(Genre).all()

    def get_all_with_pagination(self, page):
        """
        Метод получения всех записей из БД с учетом пагинации
        :param page: номер страницы
        :return: object: результат запроса
        """
        query = self.session.query(Genre).paginate(page=page, error_out=False, max_per_page=ITEMS_PER_PAGE)
        return query.items

    def get_all_sorted_asc(self):
        """
        Метод получения всех записей из БД с учетом порядка вывода
        :return: object: результат запроса
        """
        return self.session.query(Genre).order_by(Genre.name).all()

    def get_all_sorted_desc(self):
        """
        Метод получения всех записей из БД с учетом порядка вывода
        :return: object: результат запроса
        """
        return self.session.query(Genre).order_by(desc(Genre.name)).all()

    def get_all_sort_and_page_asc(self, page):
        """
        Метод получения всех записей из БД с учетом порядка вывода и пагинации
        :return: object: результат запроса
        """
        query = self.session.query(Genre).order_by(Genre.name).paginate(page=page,
                                                                        error_out=False,
                                                                        max_per_page=ITEMS_PER_PAGE)
        return query.items

    def get_all_sort_and_page_desc(self, page):
        """
        Метод получения всех записей из БД с учетом порядка вывода и пагинации
        :return: object: результат запроса
        """
        query = self.session.query(Genre).order_by(desc(Genre.name)).paginate(page=page,
                                                                              error_out=False,
                                                                              max_per_page=ITEMS_PER_PAGE)
        return query.items

    def create(self, genre_d):
        ent = Genre(**genre_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, gid):
        genre = self.get_by_id(gid)
        self.session.delete(genre)
        self.session.commit()

    def update(self, genre_d):
        genre = self.get_by_id(genre_d.get("id"))
        genre.name = genre_d.get("name")

        self.session.add(genre)
        self.session.commit()

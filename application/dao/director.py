from application.constants import ITEMS_PER_PAGE
from application.dao.models import Director
from sqlalchemy import desc


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        return self.session.query(Director).get(bid)

    def get_all(self):
        return self.session.query(Director).all()

    def create(self, director_d):
        ent = Director(**director_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, rid):
        director = self.get_one(rid)
        self.session.delete(director)
        self.session.commit()

    def update(self, director_d):
        director = self.get_one(director_d.get("id"))
        director.name = director_d.get("name")

        self.session.add(director)
        self.session.commit()

    def get_all_with_pagination(self, page):
        """
        Метод получения всех записей из БД с учетом пагинации
        :param page: номер страницы
        :return: object: результат запроса
        """
        query = self.session.query(Director).paginate(page=page, error_out=False, max_per_page=ITEMS_PER_PAGE)
        return query.items

    def get_all_sorted_asc(self):
        """
        Метод получения всех записей из БД с учетом порядка вывода
        :return: object: результат запроса
        """
        return self.session.query(Director).order_by(Director.name).all()

    def get_all_sorted_desc(self):
        """
        Метод получения всех записей из БД с учетом порядка вывода
        :return: object: результат запроса
        """
        return self.session.query(Director).order_by(desc(Director.name)).all()

    def get_all_sort_and_page_asc(self, page):
        """
        Метод получения всех записей из БД с учетом порядка вывода и пагинации
        :return: object: результат запроса
        """
        query = self.session.query(Director).order_by(Director.name).paginate(page=page,
                                                                              error_out=False,
                                                                              max_per_page=ITEMS_PER_PAGE)
        return query.items

    def get_all_sort_and_page_desc(self, page):
        """
        Метод получения всех записей из БД с учетом порядка вывода и пагинации
        :return: object: результат запроса
        """
        query = self.session.query(Director).order_by(desc(Director.name)).paginate(page=page,
                                                                                    error_out=False,
                                                                                    max_per_page=ITEMS_PER_PAGE)
        return query.items

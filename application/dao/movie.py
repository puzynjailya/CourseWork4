from sqlalchemy import desc

from application.constants import ITEMS_PER_PAGE
from application.dao.models.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        return self.session.query(Movie).get(bid)

    def get_all(self):
        return self.session.query(Movie).all()

    def get_by_director_id(self, val):
        return self.session.query(Movie).filter(Movie.director_id == val).all()

    def get_by_genre_id(self, val):
        return self.session.query(Movie).filter(Movie.genre_id == val).all()

    def get_by_year(self, val):
        return self.session.query(Movie).filter(Movie.year == val).all()

    def create(self, movie_d):
        ent = Movie(**movie_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, rid):
        movie = self.get_one(rid)
        self.session.delete(movie)
        self.session.commit()

    def update(self, movie_d):
        movie = self.get_one(movie_d.get("id"))
        movie.title = movie_d.get("title")
        movie.description = movie_d.get("description")
        movie.trailer = movie_d.get("trailer")
        movie.year = movie_d.get("year")
        movie.rating = movie_d.get("rating")
        movie.genre_id = movie_d.get("genre_id")
        movie.director_id = movie_d.get("director_id")

        self.session.add(movie)
        self.session.commit()

    def get_all_with_pagination(self, page):
        """
        Метод получения всех записей из БД с учетом пагинации
        :param page: номер страницы
        :return: object: результат запроса
        """
        query = self.session.query(Movie).paginate(page=page, error_out=False, max_per_page=ITEMS_PER_PAGE)
        return query.items

    def get_all_sorted_asc(self):
        """
        Метод получения всех записей из БД с учетом порядка вывода
        :return: object: результат запроса
        """
        return self.session.query(Movie).order_by(Movie.year).all()

    def get_all_sorted_desc(self):
        """
        Метод получения всех записей из БД с учетом порядка вывода
        :return: object: результат запроса
        """
        return self.session.query(Movie).order_by(desc(Movie.year)).all()

    def get_all_sort_and_page_asc(self, page):
        """
        Метод получения всех записей из БД с учетом порядка вывода и пагинации
        :return: object: результат запроса
        """
        query = self.session.query(Movie).paginate(page=page, error_out=False, max_per_page=ITEMS_PER_PAGE).order_by(Movie.year)

        return query.items

    def get_all_sort_and_page_desc(self, page):
        """
        Метод получения всех записей из БД с учетом порядка вывода и пагинации
        :return: object: результат запроса
        """
        query = self.session.query(Movie).order_by(desc(Movie.year)).paginate(page=page,
                                                                              error_out=False,
                                                                              max_per_page=ITEMS_PER_PAGE)
        return query.items

from application.dao.movie import MovieDAO
from application.exceptions import ItemNotFound
from application.schemas.movie import MovieSchema


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, bid, return_obj=False):
        """
        Получение данных о фильме
        :param bid: индекс фильма
        :param return_obj: флаг возврата объекта. По умолчанию возвращает сериализованные данные
        :return: Сериализованные данные или объект
        """
        movie = self.dao.get_one(bid)
        if not movie:
            raise ItemNotFound

        # Если флаг возврата объекта есть, то возвращаем объект
        if return_obj:
            return movie
        # Иначе возвращаем сериализованные данные
        return MovieSchema().dump(movie)

    def get_all(self, director, genre, year, page, status):
        """
        Сервис получения списка фильмов.
        При отстутсвии параметров отображаются все фильмы
        При наличии параметров отображаются фильмы в соответствии с заданными параметрами
        director: str - значение полученного параметра director_id
        genre: str - значение полученного параметра genre_id
        year: str - значение полученного параметра year
        page: str - значение полученного параметра page
        status: str - значение полученного параметра status
        :return: сериализованный список фильмов
        """
        # Если задан director_id
        if director:
            all_movies = self.dao.get_by_director_id(director)
            return MovieSchema(many=True).dump(all_movies)

        # Если задан genre_id
        elif genre:
            all_movies = self.dao.get_by_genre_id(genre)
            return MovieSchema(many=True).dump(all_movies)

        elif year:
            all_movies = self.dao.get_by_year(year)
            return MovieSchema(many=True).dump(all_movies)

        # Если задан параметр page:
        elif page and not status:
            # Возвращаем 12 записей с ограничением страницы
            # т.е. для страницы 1 - вернется offset(0) и выведутся первые 12 записей
            # Для страницы два вернется offset(12) и т.д.

            page = int(page)
            all_movies = self.dao.get_all_with_pagination(page=page)
            return MovieSchema(many=True).dump(all_movies)

        elif status and not page:

            status = status.upper()
            if status == 'NEW':
                # Если задан параметр status = NEW, то возвращаем сортированный запрос по name по возрастанию
                all_movies = self.dao.get_all_sorted_desc()
            else:
                # Если задан параметр status != NEW, то возвращаем сортированный запрос по name по убыванию
                all_movies = self.dao.get_all_sorted_asc()

            return MovieSchema(many=True).dump(all_movies)

        elif page and status:

            page = int(page)
            status = status.upper()

            # Если заданы page и status, то возвращаем запрос учитывающий пагинацию и сортировку (как выше)
            # Если задан как new
            if status == 'NEW':
                all_movies = self.dao.get_all_sort_and_page_desc(page=page)

            # Если задан как old
            elif status == 'OLD':
                all_movies = self.dao.get_all_sort_and_page_asc(page=page)

            # в противном случае возвращаем без order_by
            else:
                all_movies = self.dao.get_all_with_pagination(page=page)

            return MovieSchema(many=True).dump(all_movies)

        # Если фильтры пустые, то возвращаем все записи
        else:
            all_movies = self.dao.get_all()
            return MovieSchema(many=True).dump(all_movies)

    def create(self, movie_d):
        return self.dao.create(movie_d)

    def update(self, movie_d):
        self.dao.update(movie_d)

    def delete(self, rid):
        self.dao.delete(rid)

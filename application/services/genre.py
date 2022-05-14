from application.dao import GenreDAO
from application.exceptions import ItemNotFound
from application.schemas.genre import GenreSchema


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_item_by_id(self, gid, return_obj=False):
        """
        Получение данных о жанре
        :param gid: индекс жанра
        :param return_obj: флаг возврата объекта. По умолчанию возвращает сериализованные данные
        :return: Сериализованные данные или объект
        """
        genre = self.dao.get_by_id(gid)
        if not genre:
            raise ItemNotFound

        # Если флаг возврата объекта есть, то возвращаем объект
        if return_obj:
            return genre
        # Если нет, то возвращаем сериализованные данные
        return GenreSchema().dump(genre)

    def get_all_genres(self, page, status):
        # Если задан параметр page:
        if page:
            # Возвращаем 12 записей с ограничением страницы
            # т.е. для страницы 1 - вернется offset(0) и выведутся первые 12 записей
            # Для страницы два вернется offset(12) и т.д.
            page = int(page)
            genres = self.dao.get_all_with_pagination(page=page)

        if status:
            status = status.upper()
            if status == 'ASC':
                # Если задан параметр status = ASC, то возвращаем сортированный запрос по name по возрастанию
                genres = self.dao.get_all_sorted_asc()

            else:
                # Если задан параметр status != ASC, то возвращаем сортированный запрос по name по убыванию
                genres = self.dao.get_all_sorted_desc()

        if page and status:
            page = int(page)
            status = status.upper()
            # Если заданы page и status, то возвращаем запрос учитывающий пагинацию и сортировку (как выше)
            if status == 'ASC':
                genres = self.dao.get_all_sort_and_page_asc(page=page)
            else:
                genres = self.dao.get_all_sort_and_page_desc(page=page)

        if not page and not status:
            # Если параметров нет, то возвращаем просто все записи
            genres = self.dao.get_all()

        return GenreSchema(many=True).dump(genres)

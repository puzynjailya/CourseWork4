from application.dao.director import DirectorDAO
from application.exceptions import ItemNotFound
from application.schemas.director import DirectorSchema


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, did):
        director = self.dao.get_one(did)
        if not director:
            raise ItemNotFound
        return DirectorSchema().dump(director)

    def get_all_directors(self, page, status):
        # Если задан параметр page:
        if page:
            # Возвращаем 12 записей с ограничением страницы
            # т.е. для страницы 1 - вернется offset(0) и выведутся первые 12 записей
            # Для страницы два вернется offset(12) и т.д.
            page = int(page)
            directors = self.dao.get_all_with_pagination(page=page)

        if status:
            status = status.upper()
            if status == 'ASC':
                # Если задан параметр status = ASC, то возвращаем сортированный запрос по name по возрастанию
                directors = self.dao.get_all_sorted_asc()

            else:
                # Если задан параметр status != ASC, то возвращаем сортированный запрос по name по убыванию
                directors = self.dao.get_all_sorted_desc()

        if page and status:
            page = int(page)
            status = status.upper()
            # Если заданы page и status, то возвращаем запрос учитывающий пагинацию и сортировку (как выше)
            if status == 'ASC':
                directors = self.dao.get_all_sort_and_page_asc(page=page)
            else:
                directors = self.dao.get_all_sort_and_page_desc(page=page)

        if not page and not status:
            # Если параметров нет, то возвращаем просто все записи
            directors = self.dao.get_all()

        return DirectorSchema(many=True).dump(directors)

    def create(self, director_d):
        return self.dao.create(director_d)

    def update(self, did, director_d):
        """
        Сервис обновления данных режиссера
        :param did: ИД режиссера
        :param director_d: данные для обновления
        :return: dao
        """
        director = self.get_one(did)
        director.name = director_d.get("name")
        self.dao.update(director_d)
        return director

    def delete(self, did):
        self.dao.delete(did)

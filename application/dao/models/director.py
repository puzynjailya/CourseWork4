from application.dao.models.base import BaseMixin
from application.db_initialization import db


# Создаем класс для Режиссеров
class Director(BaseMixin, db.Model):
    __tablename__ = 'directors'

    name = db.Column(db.String(100), nullable=False, unique=True)

    def __repr__(self):
        return f"<Director '{self.name.title()}'>"


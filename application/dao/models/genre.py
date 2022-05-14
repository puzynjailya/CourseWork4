from application.dao.models.base import BaseMixin
from application.dao.models.favorite import favorite_genres
from application.db_initialization import db


class Genre(BaseMixin, db.Model):
    __tablename__ = "genres"

    name = db.Column(db.String(100), unique=True, nullable=False)
    users = db.relationship('User', secondary=favorite_genres, back_populates="genres")

    def __repr__(self):
        return f"<Genre '{self.name.title()}'>"

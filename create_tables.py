from application.config import DevelopmentConfig
from application.dao.models import *  # noqa F401, F403
from application.server import create_app
from application.db_initialization import db

app = create_app(DevelopmentConfig)

with app.app_context():
    db.drop_all()
    db.create_all()

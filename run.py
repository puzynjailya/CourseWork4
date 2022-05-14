from application.config import DevelopmentConfig
from application.dao.models import Director, Movie, Genre, User
from application.server import create_app, db

app = create_app(DevelopmentConfig)


@app.shell_context_processor
# ХЗ Вообще что он делает
def shell():
    return {
        "db": db,
        "Genre": Genre,
        "Director": Director,
        "Movie": Movie,
        "User": User
    }
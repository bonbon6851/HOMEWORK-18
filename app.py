from flask_restx import Api
from flask import Flask
from setup_db import db
from config import Config
from views.movies import movie_ns
from views.genres import genre_ns
from views.directors import director_ns
from data.create_table import create_table


def create_app(config_app: Config) -> Flask:
    """
    Функция создания Flask приложения
    """
    application = Flask(__name__)
    application.config.from_object(config_app)
    application.app_context().push()
    return application


def register_extensions(application: Flask):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(movie_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)


def create_data(application: Flask):
    """
    Функция создания базы данных
    """
    with application.app_context():
        db.drop_all()
        db.create_all()
        create_table()


if __name__ == '__main__':
    app = create_app(Config())
    register_extensions(app)
    create_data(app)
    app.run(port=9000)

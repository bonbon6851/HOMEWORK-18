from setup_db import db
from dao.model.movies import Movie
from dao.model.directors import Director
from dao.model.genres import Genre
from data.table_data import data


def create_table():
    for movie in data["movies"]:
        m = Movie(
            id=movie["pk"],
            title=movie["title"],
            description=movie["description"],
            trailer=movie["trailer"],
            year=movie["year"],
            rating=movie["rating"],
            genre_id=movie["genre_id"],
            director_id=movie["director_id"],
        )
        with db.session.begin():
            db.session.add(m)

    for director in data["directors"]:
        d = Director(
            id=director["pk"],
            name=director["name"],
        )
        with db.session.begin():
            db.session.add(d)

    for genre in data["genres"]:
        d = Genre(
            id=genre["pk"],
            name=genre["name"],
        )
        with db.session.begin():
            db.session.add(d)

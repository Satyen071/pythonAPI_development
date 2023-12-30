from datetime import datetime

from app.base import session, Base, engine
from app.model.movie import Movie

Base.metadata.create_all(engine)


def save_movie(data):
    # print(data)
    release_date = data["release_date"]
    print(release_date)
    movie = Movie(data["title"], datetime.strptime(release_date, '%d-%m-%Y').date())
    print("movie object")
    # print(movie)
    session.add(movie)
    session.commit()
    return movie


def get_all_movie():
    movies = session.query(Movie).all()
    return _get_response_format(movies)


def _get_response_format(movies):
    movie_data = [{"movieName": m.title, "releaseDate": m.release_date} for m in movies]
    print(movie_data)
    return movie_data

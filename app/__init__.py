from flask import Flask
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.controllers.MovieController import movie_bp
from app.controllers.ProductController import home_bp

app = Flask(__name__)
app.register_blueprint(home_bp, url_prefix='/home')
app.register_blueprint(movie_bp, url_prefix='/movie')

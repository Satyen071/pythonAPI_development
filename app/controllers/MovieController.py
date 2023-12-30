import json

import jsonpickle
import bson
from flask import jsonify, request
from flask import Blueprint
from app.service.movie_service import *

movie_bp = Blueprint('movie', __name__)


@movie_bp.route('/create_movie', methods=['POST'])
def create_data():
    data = request.json
    # print(data)
    movie = save_movie(data)
    response = json.dumps(vars(movie), indent=4, sort_keys=True, default=str)
    print(response)
    print(json.dumps(vars(movie), indent=4, sort_keys=True, default=str))
    return response


@movie_bp.route('/get_all_movie', methods=['GET'])
def get_data():
    response = get_all_movie()

    return response

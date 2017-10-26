from flask import jsonify, make_response

from . import main


@main.route('/', methods=['GET'])
def index():
    return make_response(jsonify(dict(message='hello world')))

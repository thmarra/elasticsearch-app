from flask import jsonify
from flask import make_response


def json_response(data, code=200):
    return make_response(jsonify(data), code)
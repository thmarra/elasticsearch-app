from flask import Flask, request
from .utils.json import *
from .utils import defaults
from .utils.settings import config

app = Flask(__name__)


@app.route('/')
def search():
    """  """
    return json_response({
        'username': 'teste',
        'email': 'teste@teste.com',
        'id': 123
    })


@app.route('/owners')
def owners():
    """  """
    return json_response(defaults.owners())


@app.route('/categories')
def categories():
    """  """
    return json_response(defaults.categories())


@app.route('/upload')
def upload():
    """  """
    return ""

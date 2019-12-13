from flask import Blueprint
from flask_cors import cross_origin
from ..utils.json import *

default_values = Blueprint('default', __name__)

_AUTHORS = [{
        'id': 'a-1',
        'name': 'Romina Hadid',
        'image': 'team-3-800x800.jpg'
    }, {
        'id': 'a-2',
        'name': 'Alexander Smith',
        'image': 'team-1-800x800.jpg'
    }, {
        'id': 'a-3',
        'name': 'Jane Doe',
        'image': 'team-1-800x800.jpg'
    }, {
        'id': 'a-4',
        'name': 'Rae Tompson',
        'image': 'team-4-800x800.jpg'
    }]

_CATEGORIES = [{
        'id': 'c-1',
        'description': 'Manuais'
    }, {
        'id': 'c-2',
        'description': 'Certidões'
    }, {
        'id': 'c-3',
        'description': 'Arquivos'
    }, {
        'id': 'c-4',
        'description': 'Contas / boletos'
    }, {
        'id': 'c-5',
        'description': 'Legislação'
    }, {
        'id': 'c-6',
        'description': 'Tutoriais'
    }, {
        'id': 'c-7',
        'description': 'Outros'
    }]


@default_values.route('/authors')
@cross_origin()
def authors():
    """  """
    return json_response(_AUTHORS)


@default_values.route('/categories')
@cross_origin()
def categories():
    """  """
    return json_response(_CATEGORIES)

from flask import Blueprint
from flask_cors import cross_origin
from ..utils.json import *

default_values = Blueprint('default', __name__)

_AUTHORS = [{
        'id': 'a1',
        'name': 'Romina Hadid',
        'image': 'team-3-800x800.jpg'
    }, {
        'id': 'a2',
        'name': 'Alexander Smith',
        'image': 'team-1-800x800.jpg'
    }, {
        'id': 'a3',
        'name': 'Jane Doe',
        'image': 'team-1-800x800.jpg'
    }, {
        'id': 'a4',
        'name': 'Rae Tompson',
        'image': 'team-4-800x800.jpg'
    }]

_PUBLISHERS = [{
        'id': 'p1',
        'name': 'Grupo Lund'
    }, {
        'id': 'p2',
        'name': 'Editora Três'
    }, {
        'id': 'p3',
        'name': 'Devir Livraria'
    }, {
        'id': 'p4',
        'name': 'IBEP'
    }, {
        'id': 'p5',
        'name': 'Companhia das Letras'
    }, {
        'id': 'p6',
        'name': 'JBC'
    }, {
        'id': 'p7',
        'name': 'Outros'
    }]


@default_values.route('/authors')
@cross_origin()
def authors():
    """  """
    return json_response(_AUTHORS)


@default_values.route('/publishers')
@cross_origin()
def publishers():
    """  """
    return json_response(_PUBLISHERS)

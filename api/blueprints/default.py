from flask import Blueprint, render_template, abort
from ..utils.json import *

default_values = Blueprint('default', __name__)


@default_values.route('/authors')
def authors():
    """  """
    return json_response([{
        'id': 1,
        'name': 'Romina Hadid',
        'image': 'team-3-800x800.jpg'
    }, {
        'id': 2,
        'name': 'Alexander Smith',
        'image': 'team-1-800x800.jpg'
    }, {
        'id': 3,
        'name': 'Jane Doe',
        'image': 'team-1-800x800.jpg'
    }, {
        'id': 4,
        'name': 'Rae Tompson',
        'image': 'team-4-800x800.jpg'
    }])


@default_values.route('/categories')
def categories():
    """  """
    return json_response([{
        'id': 1,
        'description': 'Manuais'
    }, {
        'id': 2,
        'description': 'Certidões'
    }, {
        'id': 3,
        'description': 'Arquivos'
    }, {
        'id': 4,
        'description': 'Contas / boletos'
    }, {
        'id': 5,
        'description': 'Legislação'
    }, {
        'id': 6,
        'description': 'Tutoriais'
    }, {
        'id': 7,
        'description': 'Outros'
    }])

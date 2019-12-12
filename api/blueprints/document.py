from flask import Blueprint, request
from ..utils.json import *
from ..utils.file import convert_to_text
from ..utils.communication import ElasticsearchClient

documents = Blueprint('documents', __name__)


@documents.route('/document', methods=['GET'])
def find():
    """  """
    return json_response({'say': 'Hi!'})


@documents.route('/document', methods=['POST'])
def create():
    """  """
    category = request.form.get('category')
    data = {
        'author_id': request.form.get('author'),
        'tags': request.form.getlist('tags[]'),
        'file': request.files['file'],
        'contents': None
    }

    if not category:
        return json_response({'error': 'The field category is required'}, 400)
    if not data.get('author_id'):
        return json_response({'error': 'The field author is required'}, 400)
    if not data.get('file'):
        return json_response({'error': 'The field file is required'}, 400)

    data['contents'] = convert_to_text(data['file'])

    es = ElasticsearchClient(category)
    success, id = es.insert(body=data)

    if not success:
        return json_response({'error': 'Could not save file'}, 500)

    file = es.find_id(id)

    return json_response({'file': file}, 201)


@documents.route('/document', methods=['PUT'])
def update():
    """  """
    pass


@documents.route('/document/change-category', methods=['PUT'])
def change_category():
    """  """
    pass
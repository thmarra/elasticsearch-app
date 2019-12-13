from flask import Blueprint, request
from flask_cors import cross_origin
from ..utils.json import *
from ..utils.communication import ElasticsearchClient
from ..business.validate import is_valid_request_new_document


documents = Blueprint('documents', __name__)


@documents.route('/document', methods=['GET'])
@cross_origin()
def find():
    """  """
    es = ElasticsearchClient('c-*')
    data = es.search(query={})
    return json_response(data)


@documents.route('/document', methods=['POST'])
@cross_origin()
def create():
    """  """
    try:
        data = is_valid_request_new_document(request)
        index = data.get('category_id')

        es = ElasticsearchClient(index)
        created, _id = es.insert(body=data)

        if not created:
            return json_response({'error': 'Could not save file'}, 500)

        response = es.find_id(id=_id)

        return json_response(response, 201)
    except TypeError as e:
        return json_response({'error': str(e)}, 400)


@documents.route('/document', methods=['PUT'])
@cross_origin()
def update():
    """  """
    pass


@documents.route('/document/change-category', methods=['PUT'])
@cross_origin()
def change_category():
    """  """
    pass
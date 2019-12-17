from flask import Blueprint, request
from flask_cors import cross_origin
from ..utils.json import *
from ..utils.communication import ElasticsearchClient
from ..business.validate import is_valid_request_new_document


documents = Blueprint('documents', __name__)
_INDEX = 'arquivos'


@documents.route('/document', methods=['GET'])
@cross_origin()
def find():
    """  """
    publisher = 'p5'
    search = 'contribuinte'
    query = {
        "_source": [
            "file",
            "author",
            "publisher",
            "tags",
            "published_at",
            "imported_at"
        ],
        "query": {
            "bool": {
                "filter": {
                    "term": {
                        "publisher.id": publisher
                    }
                },
                "must": [
                    {
                        "multi_match": {
                            "query": search,
                            "fields": [
                                "contents",
                                "file",
                                "tags",
                                "author.name"
                            ],
                            "type": "best_fields",
                            "fuzziness": 1
                        }
                    }
                ]
            }
        },
        "highlight": {
            "number_of_fragments": 1,
            "order": "score",
            "pre_tags": """<span class="highlight">""",
            "post_tags": "</span>",
            "fields": {
                "contents": {},
                "file": {},
                "tags": {},
                "author.name": {}
            }
        }
    }

    es = ElasticsearchClient(_INDEX)
    data = es.search(query=query)
    return json_response(data)


@documents.route('/document', methods=['POST'])
@cross_origin()
def create():
    """  """
    try:
        data = is_valid_request_new_document(request)

        es = ElasticsearchClient(_INDEX)
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


@documents.route('/document/change-publisher', methods=['PUT'])
@cross_origin()
def change_publisher():
    """  """
    pass
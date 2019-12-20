from flask import Blueprint, request
from flask_cors import cross_origin
from ..utils.json import *
from ..utils.communication import ElasticsearchClient
from ..business.validate import is_valid_request_new_document
from datetime import datetime
import re


documents = Blueprint('documents', __name__)
_INDEX = 'arquivos'


def _look_for_single_date(string):
    pattern = re.compile('^([0-9]{2}\/[0-9]{2}\/[0-9]{4}|[0-9]{2}-[0-9]{2}-[0-9]{4})$')
    match = pattern.findall(string)
    if len(match) == 1 and '-' not in match[0]:
        return datetime.strptime(match[0], '%d/%m/%Y').date()
    if len(match) == 1 and '-' in match[0]:
        return datetime.strptime(match[0], '%d-%m-%Y').date()
    return None


@documents.route('/document', methods=['GET'])
@cross_origin()
def find():
    """  """
    publisher = request.args.get('publisher')
    search = request.args.get('search')

    if not publisher:
        return json_response({'error': 'The field publisher is required'}, 400)

    source = [
        "file",
        "author",
        "publisher",
        "tags",
        "published_at",
        "imported_at"
    ]

    query = {
        "query": {
            "bool": {
                "filter": {
                    "term": {
                        "publisher.id": publisher
                    }
                }
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

    if search:
        must_search = [{
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
        }]

        date = _look_for_single_date(search)
        if date:
            # TODO adicionar ordem pela data abaixo crescente
            must_search.append({
                "range": {
                    "published_at": {
                        "gte": "{} 00:00:00".format(date),
                        "lte": "now"
                    }
                }
            })

        query['query']['bool']['must'] = must_search

    es = ElasticsearchClient(_INDEX)
    data = es.search(query=query, source=source)
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
from elasticsearch import Elasticsearch, helpers
from .settings import config


class ElasticsearchClient(object):

    def __init__(self, index):
        self.index = index
        self.__connect()

    def __connect(self):
        self.client = Elasticsearch([config('ELASTICSEARCH_HOST', 'localhost')],
                                    port=config('ELASTICSEARCH_PORT', 9200),
                                    # sniff before doing anything
                                    sniff_on_start=False,
                                    # refresh nodes after a node fails to respond
                                    sniff_on_connection_fail=False,
                                    )

    def change_index(self, index):
        self.index = index

    def bulk(self, body, action='index'):
        payload = []
        if type(body) is list:
            for item in body:
                payload.append({
                    '_op_type': action,
                    '_index': self.index,
                    '_source': item
                })
        else:
            payload.append({
                '_op_type': action,
                '_index': self.index,
                '_source': body
            })
        took, res = helpers.bulk(self.client, actions=payload)
        return took, (took == len(payload))

    def insert(self, body, id=None):
        res = self.client.index(index=self.index, body=body, id=id)
        created = res['result'] == 'created'
        _id = None
        if '_id' in res:
            _id = res['_id']
        return created, _id

    def find_id(self, id):
        res = self.client.get(index=self.index, id=id)
        return res

    def search(self, query, source):
        print(self.index, query)
        # query['_source_include'] = source
        return self.client.search(index=self.index, body=query, params={'_source_includes': source})

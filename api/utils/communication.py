from elasticsearch import Elasticsearch
from .settings import config


class ElasticsearchClient(object):

    def __init__(self, index):
        self.index = index
        self.__connect()

    def __connect(self):
        self.client = Elasticsearch([config('ELASTICSEARCH_HOST', 'localhost')],
                                    port=config('ELASTICSEARCH_PORT', 9200),
                                    # sniff before doing anything
                                    sniff_on_start=True,
                                    # refresh nodes after a node fails to respond
                                    sniff_on_connection_fail=True,
                                    )

    def change_index(self, index):
        self.index = index

    def insert(self, body, id=None):
        res = self.client.index(index=self.index, body=body, id=id)
        created = res['result'] == 'created'
        _id = None
        if '_id' in res:
            _id = res['_id']
        return created, _id

    def find_id(self, id):
        res = self.client.get(index=self.index, id=id)
        print(res)

    def search(self, query):
        return self.client.search(index=self.index, body=query)

from elasticsearch import Elasticsearch


es = Elasticsearch(['http://localhost'])

query = {
    "query": {
        "simple_query_string": {
            "query": """
            guia*
            """,
            "fields": ["titulo^3", "categoria^2", "conteudo"],
            "default_operator": "or",
            "fuzzy_max_expansions": 30,
            "fuzzy_prefix_length": 5,
            "auto_generate_synonyms_phrase_query": True
        }
    },
    "highlight": {
        "number_of_fragments": 3,
        "order": "score",
        "pre_tags": """<span class="highlight">""",
        "post_tags": "</span>",
        "fields": {
            "*": {}
        }
    }
}


result = es.search(index='teste', body=query)
print(result)
## Query x Filter
- Query possui relevância, enquanto filter não;
- Filter é cacheavel, query não;

Se precisa organizar por relevância, use Query, caso contrário, use Filter.

## Term x Full text (match)
- *Term:* exact match - pesquisa direto no inverted index
- *Match:* são analizadas antes de ir para o inverted index, normalizando a pesquisa e o resultado

## Mapping
```
{
  "settings": {
    "analysis": {
      "filter": {
        "brazilian_stop": {
          "type": "stop",
          "stopwords": "_brazilian_"
        },
        "brazilian_keywords": {
          "type": "keyword_marker",
          "keywords": [
            "exemplo"
          ]
        },
        "brazilian_stemmer": {
          "type": "stemmer",
          "language": "brazilian"
        },
        "eneagrama": {
          "type": "edge_ngram",
          "min_gram": 1,
          "max_gram": 3
        }
      },
      "analyzer": {
        "rebuilt_brazilian": {
          "tokenizer": "standard",
          "filter": [
            "lowercase",
            "brazilian_stop",
            "brazilian_keywords",
            "brazilian_stemmer",
            "eneagrama"
          ]
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "categoria": {
        "type": "text",
        "fields": {
          "keyword": {
            "type": "keyword",
            "ignore_above": 256
          }
        }
      },
      "conteudo": {
        "type": "text",
        "fields": {
          "keyword": {
            "type": "keyword",
            "ignore_above": 256
          }
        }
      },
      "importacao": {
        "type": "date",
        "format": "yyyy-MM-dd HH:mm:ss"
      },
      "pagina": {
        "type": "text",
        "fields": {
          "keyword": {
            "type": "keyword",
            "ignore_above": 256
          }
        }
      },
      "titulo": {
        "type": "text",
        "fields": {
          "keyword": {
            "type": "keyword",
            "ignore_above": 256
          }
        }
      }
    }
  }
}
```

## Search
```
GET /teste/_search
{
  "query": {
    "simple_query_string": {
      "query": """
      guia
      """,
      "fields": [
        "titulo^3",
        "categoria^2",
        "conteudo"
      ],
      "default_operator": "or",
      "auto_generate_synonyms_phrase_query": true
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
```

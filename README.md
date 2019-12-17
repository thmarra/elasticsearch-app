# Testando o ElasticSearch

## Objetivo e regras negociais:
Para testar o comportamento do elasticsearch foi criada uma aplicação que visa salvar arquivos, obedecendo as seguintes regras negociais:
1. A aplicação deve receber e indexar arquivos PDF;
2. Cada arquivo precisa necessariamente de uma categoria e um autor;
3. As categorias possuem um ou mais autores;
4. Cada autor pertence a apenas uma categoria;
5. Os autores podem mudar de categoria;
6. Os arquivos não podem mudar de autor;

### Modelo normalizado:
Um dos objetivos do teste é descobrir a melhor forma de importar para o ElasticSearch dados que estão normalizados no banco relacional em uma estrutura similar a seguinte:

![Modelo normalizado](https://github.com/thmarra/elasticsearch-app/blob/master/modelo_normalizado.png)

## Endpoints:
- Lista com pesquisa de arquivos
- Alterar arquivo (tags)
- Alterar categoria

## Indexação dos dados:
A categoria será um campo obrigatório em todas as pesquisas. É preciso enviar um ID para iniciar a pesquisa.

Os demais campos a serem pesquisados são:
- Autor
- Tags
- Data de criação
- Data de envio
- Conteúdo do arquivo

### Mappings:
```
PUT /arquivos
{
  "settings": {
    "analysis": {
      "filter": {
        "brazilian_stop": {
          "type": "stop",
          "stopwords": "_brazilian_"
        },
        "brazilian_stemmer": {
          "type": "stemmer",
          "language": "brazilian"
        },
        "stemmer_plural_portugues": {
          "type": "stemmer",
          "name": "minimal_portuguese"
        },
        "split_on_change_case": {
          "type": "word_delimiter",
          "preserve_original": true,
          "split_on_numerics": false
        }
      },
      "analyzer": {
        "rebuilt_brazilian": {
          "tokenizer": "standard",
          "filter": [
            "split_on_change_case",
            "lowercase",
            "asciifolding",
            "brazilian_stop",
            "brazilian_stemmer",
            "stemmer_plural_portugues"
          ]
        },
        "basic_analyzer": {
          "tokenizer": "standard",
          "filter": [
            "lowercase",
            "asciifolding"
          ]
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "author": {
        "properties": {
          "id": {
            "type": "keyword"
          },
          "image": {
            "type": "keyword"
          },
          "name": {
            "type": "text"
          }
        }
      },
      "publisher": {
        "properties": {
          "id": {
            "type": "keyword"
          },
          "name": {
            "type": "text"
          }
        }
      },
      "contents": {
        "type": "text",
        "fields": {
          "raw": {
            "type": "text",
            "analyzer": "basic_analyzer"
          }
        }
      },
      "file": {
        "type": "text",
        "fields": {
          "keyword": {
            "type": "keyword",
            "ignore_above": 256
          }
        }
      },
      "imported_at": {
        "type": "date",
        "format": "yyyy-MM-dd HH:mm:ss"
      },
      "published_at": {
        "type": "date",
        "format": "yyyy-MM-dd HH:mm:ss"
      }
    }
  }
}
```
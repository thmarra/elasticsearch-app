from elasticsearch import Elasticsearch
from bs4 import BeautifulSoup
import requests
import time
import sys


es = Elasticsearch(['http://localhost'])

url = 'https://www.contabeis.com.br'

body = requests.get("{}/conteudo".format(url))
soup = BeautifulSoup(body.content, features="lxml")

for article in soup.find_all('article'):
    link = article.find('a', href=True)
    if link:
        contents = requests.get("{}/{}".format(url, link['href']))

        if contents.status_code != 200:
            continue

        page = BeautifulSoup(contents.content, features="lxml")
        section = page.find('section')
        categoria = section.find("p", attrs={"class": 'chapeu'})
        titulo = section.find("h1")
        conteudo = section.find('div', attrs={'itemprop': "articleBody"})

        data = {
            'categoria': categoria.text if categoria else None,
            'titulo': titulo.text if titulo else None,
            'conteudo': conteudo.text if conteudo else None,
            'pagina': "{}/{}".format(url, link['href']),
            'importacao': time.strftime('%Y-%m-%d %H:%M:%S'),
        }

        res = es.index(index='teste', body=data)
        _id = None
        if '_id' in res:
            _id = res['_id']
        print(_id)

    # sys.exit(1)
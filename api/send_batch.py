import os, sys
from utils.communication import ElasticsearchClient
from utils.file import convert_to_text
from multiprocessing import Process
from random import choice
from datetime import date
from math import ceil


process_count = 3
sample_files = '/home/cpmarra/Projects/python/crawlers/sample_pdf'

_TAGS = [
    ['boleto', 'arquivo', 'teste'],
    ['material didático', 'modelo', 'pdf'],
    ['ebook', 'teste', 'pdf'],
    ['documento', 'manual', 'portaria']
]

_AUTHORS = [{
        'id': 'a1',
        'name': 'Romina Hadid',
        'image': 'team-3-800x800.jpg'
    }, {
        'id': 'a2',
        'name': 'Alexander Smith',
        'image': 'team-1-800x800.jpg'
    }, {
        'id': 'a3',
        'name': 'Jane Doe',
        'image': 'team-1-800x800.jpg'
    }, {
        'id': 'a4',
        'name': 'Rae Tompson',
        'image': 'team-4-800x800.jpg'
    }]

_PUBLISHERS = [{
        'id': 'p1',
        'name': 'Grupo Lund'
    }, {
        'id': 'p2',
        'name': 'Editora Três'
    }, {
        'id': 'p3',
        'name': 'Devir Livraria'
    }, {
        'id': 'p4',
        'name': 'IBEP'
    }, {
        'id': 'p5',
        'name': 'Companhia das Letras'
    }, {
        'id': 'p6',
        'name': 'JBC'
    }, {
        'id': 'p7',
        'name': 'Outros'
    }]


def import_file(files):
    es = ElasticsearchClient('arquivos')
    for filename in files:
        with open(os.path.join(sample_files, filename), 'rb') as file:
            try:
                data = {
                    'publisher': choice(_PUBLISHERS),
                    'author': choice(_AUTHORS),
                    'tags': choice(_TAGS),
                    'contents': convert_to_text(file),
                    'file': filename,
                    'published_at': date.today().strftime("%Y-%m-%d %H:%M:%S"),
                    'imported_at': date.today().strftime("%Y-%m-%d %H:%M:%S")
                }
                # es.change_index(data['publisher']['id'])
                created, _id = es.insert(body=data)
                print(_id)
                sys.exit()
            except Exception as e:
                print(filename, str(e), sep=": ")


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def run():
    files = os.listdir(sample_files)
    per_process = ceil(len(files)/process_count)

    for chunk in chunks(files, per_process):
        p = Process(target=import_file, args=(chunk,))
        p.start()


run()

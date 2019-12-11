import os
from .utils import file as file_util
from werkzeug.utils import secure_filename
from werkzeug import FileStorage


def all():
    # TODO retornar todos os donos cadastrados
    return []


def create(name="", file=None):
    new_filename = None
    saved = False
    print(file, isinstance(file, FileStorage))
    if isinstance(file, FileStorage):
        if not file_util.allowed_image(file.filename):
            return None
        new_filename = secure_filename(file.filename)
        saved = file_util.save_file(file, new_filename)
    # TODO salvar no ES
    return {
        'name': name,
        'filename': new_filename,
        'file_exists': saved
    }


def delete(id):
    # TODO remover o dono com o id informado
    return True
from flask import Flask, flash, request, redirect, url_for
from .packages.utils.settings import config
from .packages.utils.json import *
from .packages import Owner


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = config('IMAGE_FOLDER')

# allowed = config('ALLOWED_EXTENSIONS')
# print(allowed.split(','))


@app.route('/')
def search():
    """  """
    return json_response({
        'username': 'teste',
        'email': 'teste@teste.com',
        'id': 123
    })

@app.route('/owner', methods=['GET', 'POST'])
def owner():
    """  """
    if request.method == 'POST':
        file = None
        name = request.form.get('name')
        if not name:
            return json_response({
                'error': 'The field name is required'
            }, 400)
        if 'picture' in request.files:
            file = request.files['picture']
        owner = Owner.create(name=name, file=file)
        print(owner)

    if request.method == 'GET':
        owner = {
            'username': 'teste',
            'email': 'teste@teste.com',
            'id': 123
        }
    return json_response(owner)

# @app.route('/')
# def updateConfig():
#     """  """
#     return ""

# @app.route('/')
# def upload():
#     """  """
#     return ""

# @app.route('/')
# def changeOwner():
#     """  """
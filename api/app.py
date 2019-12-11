from flask import Flask
from utils.json import *


app = Flask(__name__)


@app.route('/')
def search():
    """  """
    return json_response({
        'username': 'teste',
        'email': 'teste@teste.com',
        'id': 123
    })

# @app.route('/config')
# def config():
#     """  """
#     return "C"

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
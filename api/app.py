from flask import Flask
from .utils.json import *
from .blueprints.default import default_values
from .blueprints.document import documents

app = Flask(__name__)
app.register_blueprint(default_values)
app.register_blueprint(documents)


@app.route('/')
def search():
    """  """
    return json_response({
        'username': 'teste',
        'email': 'teste@teste.com',
        'id': 123
    })


@app.route('/upload')
def upload():
    """  """
    return ""

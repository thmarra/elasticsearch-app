from flask import Flask
from flask_cors import CORS, cross_origin
from .utils.json import *
from .blueprints.default import default_values
from .blueprints.document import documents


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app.register_blueprint(default_values)
app.register_blueprint(documents)


@app.route('/')
@cross_origin()
def search():
    """  """
    return json_response({
        'username': 'teste',
        'email': 'teste@teste.com',
        'id': 123
    })


@app.route('/upload')
@cross_origin()
def upload():
    """  """
    return ""

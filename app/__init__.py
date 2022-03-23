import os
from flask import Blueprint, Flask, redirect
from flask_restx import Api
from werkzeug.middleware.proxy_fix import ProxyFix
#from app.helper.mongo_handler import MongoHandler

""" OS ENV """
FLASK_DEBUG = int(os.getenv('FLASK_DEBUG', default=0))
ENV_NAME = os.getenv('ENV_NAME', default='test')

# Docker ENV variables
PORT = os.getenv('PORT', default='8080')

""" APPLICATION SETUP """
VERSION = 'v1'
APP_NAME = os.getenv('APP_NAME', default='flask-api')

""" Flask app SETUP """
api = Api(
    version='1.0', title='Backend Boilderplate API',
    description='Documentation for the REST API built for Backend Boilerplate',
    validate=False)

""" Flask app and RESTX SETUP """
app_blueprint = Blueprint(VERSION, __name__)
app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
app.config['SWAGGER_UI_DOC_EXPANSION'] = 'list'
app.config['RESTX_VALIDATE'] = True
app.config['RESTX_MASK_SWAGGER'] = False
app.config['ERROR_404_HELP'] = False
app.config['ERROR_INCLUDE_MESSAGE'] = False
api.init_app(app_blueprint)


@app.route('/', methods=['GET'])
def redirect_to_swagger():
    return redirect(f"/api/{VERSION}")

""" Database SETUP """
# Comment off below if mongodb is not in use
#app_db = MongoHandler()


def format_error_response(error: Exception):
    error = str(error)
    if error[0].isdigit():  # status code is in front e.g. werkzeug exceptions
        messages = error.split(' ', 1)
        return messages[-1], messages[0]
    return error, 400

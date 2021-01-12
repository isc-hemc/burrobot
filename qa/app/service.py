"""App.

Flask application declaration.

"""

from flask import Flask
from flask_cors import CORS

from app.urls import blueprint

application = Flask(__name__)
application.config.from_object("app.settings")
application.register_blueprint(blueprint, url_prefix="/")

CORS(application)

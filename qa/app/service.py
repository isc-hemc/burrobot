"""App.

Flask application declaration.

"""

from flask import Flask

from app.urls import blueprint

app = Flask(__name__)
app.config.from_object("app.settings")
app.register_blueprint(blueprint, url_prefix="/")

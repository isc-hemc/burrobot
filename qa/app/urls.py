"""Views.

Here are declared all the API endpoints.

"""

from flask import Blueprint, Flask
from flask_restful import Api

from app.resources import BurrobotResource, HealthcheckResource

blueprint = Blueprint("api", __name__)

api = Api(blueprint)

api.add_resource(HealthcheckResource, "/health")
api.add_resource(BurrobotResource, "/burrobot")

from flask import Flask
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

#initialize the app
# app = Flask(__name__, instance_relative_config=True)

# def init_app():
app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
    # return app



#Load the views
from app import views

#load the models
from app.models import database

#load tests
# from tests.test_run import TestRun

#load the config file


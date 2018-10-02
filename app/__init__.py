from flask import Flask

#initialize the app
app = Flask(__name__, instance_relative_config=True)

#Load the views
from app import views

#load the models
from app.models import database

#load tests
from tests.test_run import TestRun

#load the config file
app.config.from_object('config')

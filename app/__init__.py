from ensurepip import bootstrap
from flask import Flask
from config import DevConfig
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()

def creat_app(config_name):

    app =Flask(__name__)
    from app import views

    app.config.from_object(config_options[config_name])

    bootstrap.init_app(app)



    # Setting up configuration
    # app.config.from_object(DevConfig)
    # app.config.from_pyfile('config.py')
    return app


    
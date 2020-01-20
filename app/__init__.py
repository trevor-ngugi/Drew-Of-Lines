from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

bootstrap=Bootstrap()
db=SQLAlchemy()

def create_app(config_name):
    #initialising the app
    app=Flask(__name__)

    #setting up the configurations
    app.config.from_object(config_options[config_name])
    

    #intialising flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    #reg blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    return app


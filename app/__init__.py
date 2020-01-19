from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap

bootstrap=Bootstrap()
def create_app(config_name):
    #initialising the app
    app=Flask(__name__)

    #setting up the configurations
    app.config.from_object(config_options[config_name])
    

    #intialising flask extensions
    bootstrap.init_app(app)

    #reg blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app


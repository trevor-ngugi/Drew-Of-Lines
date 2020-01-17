from flask import Flask
from .config import DevConfig

#initialising the app
app=Flask(__name__,instance_relative_config=True)

#setting up the configurations
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')


from app import views
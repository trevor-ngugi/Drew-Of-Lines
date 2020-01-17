from flask import Flask

#initialising the app
app=Flask(__name__)

#setting up the configurations
app.config.from_object(DevConfig)
from app import views
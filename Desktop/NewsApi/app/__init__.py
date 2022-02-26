from flask import Flask
from app.config import DevConfig
from flask_bootstrap import Bootstrap

#initialize app
app = Flask(__name__, instance_relative_config= True)

#setup configurations
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')


#initialize bootstrap configuration
bootstrap = Bootstrap(app)


from app import views
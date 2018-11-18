from flask import Flask
from config import DevConfig
from flask_bootstrap import Bootstrap

#initializing application
def create_app(config_name):
    app = Flask(__name__)

# Setting up configuration
app.config.from_object(config_options[config_name])
config_options[config_name].init_app(app)

# Initializing Flask Extensions
bootstrap = Bootstrap(app)
db.init_app(app)
login_manager.init_app(app)
mail.init_app(app)

# Registering the blueprint
from .main import main as main_blueprint
app.register_blueprint(main_blueprint)


from app import views
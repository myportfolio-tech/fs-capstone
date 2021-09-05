from flask import Flask
from dotenv import load_dotenv
from flask.config import Config

load_dotenv()

def create_app(config_class=Config):
    
    app = Flask(__name__)
    app.config.from_object(Config)

    from staffer.main.routes import main
    
    app.register_blueprint(main)

    return app
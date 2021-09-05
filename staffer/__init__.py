from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
from staffer.config import Config
from dotenv import load_dotenv

db = SQLAlchemy()
load_dotenv()


def create_app(config_class=Config):    
    app = Flask(__name__)
    app.config.from_object(Config)
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://psqladmin:administrator@localhost:5432/staffer_api'
    db.init_app(app)
    
    from staffer.main.routes import main
    from staffer.employees.routes import employees
    from staffer.projects.routes import projects
    from staffer.errors.handlers import errors

    app.register_blueprint(main)
    app.register_blueprint(employees)
    app.register_blueprint(projects)
    app.register_blueprint(errors)

    return app
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from config.constants import DATABASE_URI

my_db = SQLAlchemy()


def create_app():
    app = Flask(__name__, template_folder='templates')
    # app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydb.db"
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    CORS(app)
    from routes import app_routes
    app_routes(app, my_db)

    my_db.init_app(app)
    migrate = Migrate(app, my_db)

    return app

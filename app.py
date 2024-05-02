from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'

    db.init_app(app)

    from routes import register_routes
    register_routes(app, db)

    Migrate(app, db)

    return app

# @app.route('/')
# def index():
#     data = MovieAPI().search('movie', "Limitless")
#     return data
#     # return render_template('index.html')
#
#
# @app.route('/movies/<movie_id>/casts')
# def casts(movie_id):
#     data = MovieAPI().movie_credits("TV Show", movie_id)
#     return data
#
#
# if __name__ == '__main__':
#     app.run(debug=True)

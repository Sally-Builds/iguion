import datetime
import json

from models.quote import Quote
from models.user import User
from models.categories import Category
from movieAPI import MovieAPI
from flask import request, jsonify
from validations.quote_validation import QuoteSchema
from validations.user_validation import UserSchema
from bcrypt import hashpw, gensalt, checkpw
from middlewares.auth_middleware import authenticate
import jwt
from config.constants import JWT_SECRET_KEY


def response_format(data, code=200):
    return {
                "message": "Successful",
                "data": data,
            }, code

def register_routes(app, db):
    @app.route('/')
    def index():
        return '<h3> Welcome to iGuion </h4>'

    @app.route('/quotes', methods=['POST'])
    def create_quote():
        data = request.get_json()
        schema = QuoteSchema()

        errs = schema.validate(data)
        if errs:
            return jsonify(errs), 400

        data = schema.load(data)

        quote = Quote(movie_id=data['movie_id'], quote=data['quote'], character_id=data['character_id'],
                      movie_type=data['movie_type'])

        db.session.add(quote)

        db.session.commit()

        print(Quote.query.all())

        return response_format(data, 201)

    @app.route('/quotes', methods=['GET'])
    def get_quotes():
        quotes = Quote.find_all()

        return response_format(quotes, 200)

    @app.route('/movies', methods=['GET'])
    def movies():
        data = request.args
        return MovieAPI().search(data['tv'], data['name'])

    @app.route('/movies/<movie_id>/casts', methods=['GET'])
    def casts(movie_id):
        data = MovieAPI().movie_credits("TV Show", movie_id)
        return data

    @app.route('/login', methods=['POST'])
    def login():
        data = request.get_json()

        schema = UserSchema()

        errs = schema.validate(data)

        if errs:
            return jsonify(errs), 400

        data = schema.load(data)

        user = User.query.filter_by(username=data['username']).first()

        if user is None:
            return 'username or password not correct', 401

        if not checkpw(data['password'].encode('utf-8'), user.password):
            return 'username or password not correct', 401

        now = datetime.datetime.now()
        expiration_time = now + datetime.timedelta(minutes=10)
        exp = expiration_time.timestamp()

        encoded = jwt.encode({"id": user.uid, "username": user.username, "exp": exp}, JWT_SECRET_KEY)
        return jsonify({"token": encoded})
        # return jsonify({"username": user.username, "id": user.uid}), 200

    @app.route('/signup', methods=['POST'])
    def signup():
        password = 'test1234'
        salt = gensalt()
        hashed_pw = hashpw(password.encode('utf-8'), salt)
        user = User(username="admin", password=hashed_pw)

        db.session.add(user)
        db.session.commit()

        return 'success'

    @app.route('/get_user', methods=['GET'])
    @authenticate
    def get_me(logged_in_user):
        return logged_in_user

    @app.route('/categories', methods=['POST'])
    def add_categories():
        data = request.get_json()

        res = Category.add(data['categories'])

        if not res:
            return {
                "message": "Error",
                "data": None,
                "error": "Internal Server Error"
            }, 500

        return {"message": "successful"}, 201

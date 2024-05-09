from flask import jsonify, request

from thirdParty.movieAPI import MovieAPI
from models.quotes import Quote
from validations.create_quote import CreateQuoteSchema
from marshmallow import ValidationError


def app_routes(app, db):

    @app.route('/')
    def index():
        return '<h3> Welcome to iGuion. </h3>'

    @app.route('/search')
    def search():
        keyword = request.args.get('keyword')
        movie_type = request.args.get('movie_type')
        data = MovieAPI().search(movie_type, keyword)
        return data

    @app.route('/casts')
    def movie_casts():
        movie_id = request.args.get('movie_id')
        movie_type = request.args.get('movie_type')

        data = MovieAPI().get_casts(movie_type, movie_id)

        return data

    @app.route('/quotes', methods=['POST'])
    def create_quote():
        try:
            validated_data = CreateQuoteSchema().load(request.json)
            print(validated_data)

            movie_name = MovieAPI().get_movie(validated_data['movie_type'], validated_data['movie_id'])['movie_name']

            if not movie_name:
                return {"error": {'movie_id': "no movie found with this id"}}, 400

            cast_id = MovieAPI().cast_exist_for_movie(validated_data['movie_type'], validated_data['movie_id'],
                                                      validated_data['cast_id'])

            if not cast_id:
                return {"error": {'cast_id': "no cast found with this id for this movie"}}, 400

            quote = Quote(movie_id=validated_data['movie_id'], cast_id=validated_data['cast_id'],
                          movie_type=validated_data['movie_type'],
                          quote=validated_data['quote'])
            Quote.save(quote)
            return {
                "id": quote.qid,
                "movie_type": quote.movie_type,
                "movie_name": MovieAPI().get_movie(quote.movie_type, quote.movie_id)['movie_name'],
                "cast_name": MovieAPI().get_cast(quote.cast_id)['cast_name'],
                "quote": quote.quote
            }
        except ValidationError as err:
            return jsonify({"error": err.messages}), 400

    @app.route('/quotes', methods=['GET'])
    def get_quotes():
        quotes = Quote.query.all()
        data = [{
            'id': quote.qid,
            'movie_name': MovieAPI().get_movie(quote.movie_type, quote.movie_id)['movie_name'],
                 'movie_type': quote.movie_type,
                 'cast_name': MovieAPI().get_cast(quote.cast_id)['cast_name'],
                 'images': MovieAPI().movie_images(quote.movie_type, quote.movie_id)['images'],
                 'quote': quote.quote} for quote in quotes]
        return {'quotes': data}, 200

    @app.route('/casts')
    def get_casts():
        data = MovieAPI().get_casts('tv', 1396)
        return data

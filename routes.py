from flask import jsonify, request

from thirdParty.movieAPI import MovieAPI
from models.quotes import Quote


def app_routes(app, db):
    @app.route('/search')
    def index():
        keyword = request.args.get('keyword')
        movie_type = request.args.get('movie_type')
        print(keyword, movie_type)
        # data = MovieAPI().search('tv', 'Breaking Bad')
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
        data = request.json
        data = Quote(movie_id=data['movie_id'], cast_id=data['cast_id'], movie_type=data['movie_type'],
                     quote=data['quote'])
        print(data)
        Quote.save(data)
        return 'quote created'

    @app.route('/quotes', methods=['GET'])
    def get_quotes():
        quotes = Quote.query.all()
        data = [{'movie_name': MovieAPI().get_movie(quote.movie_type, quote.movie_id)['movie_name'],
                 'movie_type': quote.movie_type,
                 'cast_name': MovieAPI().get_cast(quote.cast_id)['cast_name'],
                 'images': MovieAPI().movie_images(quote.movie_type, quote.movie_id)['images'],
                 'quote': quote.quote} for quote in quotes]
        return data, 200

    @app.route('/casts')
    def get_casts():
        data = MovieAPI().get_casts('tv', 1396)
        return data

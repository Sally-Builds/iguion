from flask import jsonify

from main import app
from thirdParty.movieAPI import MovieAPI


@app.route('/')
def index():
    data = MovieAPI().search('tv', 'Breaking Bad')
    return data


@app.route('/quotes', methods=['POST'])
def create_quote():
    return 'quote created'


@app.route('/quotes', methods=['GET'])
def get_quotes():
    return 'fetch quotes'


@app.route('/casts')
def get_casts():
    data = MovieAPI().get_casts('tv', 1396)
    return data

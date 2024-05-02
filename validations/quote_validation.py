from marshmallow import Schema, fields, pre_load, ValidationError
from enum import Enum
from movieAPI import MovieAPI


class MovieType(Enum):
    TV = 'TV Show'
    MOVIE = 'Movie'


class QuoteSchema(Schema):
    movie_id = fields.Integer(required=True)
    character_id = fields.String(required=True)
    movie_type = fields.String(required=True)
    # movie_type = fields.Enum(MovieType, required=True)
    quote = fields.String(required=True)

    @pre_load
    def process_author(self, data, **kwargs):
        movie_id = data.get('movie_id')
        movie_type = data.get('movie_type')
        if movie_id:
            does_exist = MovieAPI().does_movie_exist(movie_type, movie_id)
            if does_exist:
                pass
            else:
                raise ValidationError('Movie doesnt exist')
        return data

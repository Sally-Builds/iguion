from marshmallow import Schema, fields, validate


class CreateQuoteSchema(Schema):
    movie_id = fields.Integer(required=True)
    cast_id = fields.String(required=True)
    movie_type = fields.String(validate=validate.OneOf(['tv', 'movie']), required=True)
    quote = fields.String(required=True)

from marshmallow import Schema, fields


class CreateQuoteSchema(Schema):
    movie_id = fields.Integer(required=True)
    cast_id = fields.String(required=True)
    movie_type = fields.String(required=True)
    quote = fields.String(required=True)

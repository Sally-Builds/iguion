from marshmallow import Schema, fields, pre_load, ValidationError, validate


class UserSchema(Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)

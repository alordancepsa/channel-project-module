from marshmallow import Schema, fields

class NewCompanySchema(Schema):
    name = fields.String(required=True)
    phone = fields.String()
    flag = fields.String(required=True)

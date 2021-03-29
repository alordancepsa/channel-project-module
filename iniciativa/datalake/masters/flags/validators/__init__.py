from marshmallow import Schema, fields

class NewCompanySchema(Schema):
    name = fields.String(required=True)    
    flag = fields.String(required=True)

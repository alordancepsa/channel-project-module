from marshmallow import Schema, fields

class NewVesselSchema(Schema):
    name = fields.String(required=True)
    tp_id = fields.Number()
    so_id = fields.Number()
    co_id = fields.Number()
    imo = fields.String(required=True)


class UpdateVesselSchema(Schema):
    name = fields.String(required=True)
    tp_id = fields.Number()
    so_id = fields.Number()
    co_id = fields.Number()
    imo = fields.String(required=True)

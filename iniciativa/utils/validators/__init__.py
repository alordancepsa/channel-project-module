from marshmallow import Schema, fields

dummy = {
  "itemsPerPage": 0,
  "offset": 0,
  "query":  [
    {
      "field": "name",
      "operator": "LIKE",
      "value": "%com%"
    },
    "OR",
    [
      {
        "field": "phone",
        "operator": "NEQ",
        "value": "123"
      },
      "OR",
      {
        "field": "flag",
        "operator": "EQ",
        "value": "123"
      }
    ],
    "OR",
      {
        "field": "numeric_field",
        "operator": "EQ",
        "value": 123.0
      },
    "OR",
    {
        "field": "boolean_field",
        "operator": "EQ",
        "value": True
    }
  ]
}



class QuerySchema(Schema):
    itemsPerPage = fields.Integer(required=True)
    offset = fields.Integer(required=True)
    query = fields.Raw(required=True)

from marshmallow import Schema, fields

dummy = {
  "itemsPerPage": 0,
  "offset": 0,
  "query":  [
    {
      "field": "first_name",
      "operator": "EQ",
      "value": "Dixie"
    },
    "OR",
    [
      {
        "field": "last_name",
        "operator": "NEQ",
        "value": "Smith"
      },
      "OR",
      {
        "field": "middle_name",
        "operator": "EQ",
        "value": "Sam"
      }
    ]
  ]
}



class QuerySchema(Schema):
    itemsPerPage = fields.Integer(required=True)
    offset = fields.Integer(required=True)
    query = fields.Raw(required=True)

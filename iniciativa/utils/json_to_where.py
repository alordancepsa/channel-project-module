dummy = [
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
  ],

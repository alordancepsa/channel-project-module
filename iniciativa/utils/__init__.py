LOGICAL_OPERATORS = ("AND", "OR")

COMPARISON_OPERATORS = {
    "LT": "<",
    "GT": ">",
    "LTE": "<=",
    "GTE": ">=",
    "EQ": "=",
    "NEQ": "!=",
    "LIKE": "like"
}

def process(data, parameters={}):
    """
    :param data: JSON Object (dict). 
    :param parameters: dict.
    :return: where clause (str) built from data
    """
    where_clause = ""
    if isinstance(data, list):
        for part in data:
            if part not in LOGICAL_OPERATORS:
                where_clause += " ({}) ".format(process(part, parameters))
            else:
                where_clause += process(part, parameters)
    elif isinstance(data, dict):
        # where_clause += " {} {} %({})s ".format(data["field"], COMPARISON_OPERATORS[data["operator"]], data["field"])
        where_clause += " {} {} :{} ".format(data["field"], COMPARISON_OPERATORS[data["operator"]], data["field"])
        parameters[data["field"]] = data["value"]
    elif isinstance(data, str):
        return data
    return where_clause

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

    def get_not_repeated(field_name, params, count=0):
        """
        return not repetead field_name values in dict
        """
        current_name = "{}_rep_{}".format(field_name, count)
        if current_name not in params:
            return current_name
        
        count+=1
        return get_not_repeated(field_name, params, count)
            
            
    where_clause = ""
    if isinstance(data, list):
        for part in data:
            if part not in LOGICAL_OPERATORS:
                where_clause += " ({}) ".format(process(part, parameters))
            else:
                where_clause += process(part, parameters)
    elif isinstance(data, dict):
        # where_clause += " {} {} %({})s ".format(data["field"], COMPARISON_OPERATORS[data["operator"]], data["field"])
        field_name = data["field"] if data["field"] not in parameters else get_not_repeated(data["field"], parameters)
        where_clause += " {} {} :{} ".format(data["field"], COMPARISON_OPERATORS[data["operator"]], field_name)
        parameters[field_name] = data["value"]
    elif isinstance(data, str):
        return data
    return where_clause

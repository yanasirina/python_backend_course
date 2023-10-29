def parse_query_string(query_string):
    if not query_string:
        return {}
    query_args = query_string.split('&')
    query_dict = dict()
    for query_arg in query_args:
        arg_name, arg_value = query_arg.split('=')
        query_dict[arg_name] = arg_value
    return query_dict

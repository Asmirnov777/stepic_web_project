def divide_params(environ, start_response):
    # init_str = environ.QUERY_STRING
    body = [bytes(e + '\n', encoding='ascii') for e in environ['QUERY_STRING'].split(sep='&')]
    # pairs_list = [s.split(sep = '=', maxsplit = 1) for s in str_list]
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    # body = 'Hello, world!'
    #body = environ['QUERY_STRING'].replace('&', '\r\n')
    start_response(status, headers)
    return body

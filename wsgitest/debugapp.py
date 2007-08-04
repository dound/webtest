from wsgiobj import Request

__all__ = ['debug_app']

def debug_app(environ, start_response):
    req = Request(environ)
    if 'error' in req.queryvars:
        raise Exception('Exception requested')
    status = req.queryvars.get('status', '200 OK')
    parts = []
    for name, value in sorted(environ.items()):
        if name.upper() != name:
            value = repr(value)
        parts.append('%s: %s\n' % (name, value))
    body = ''.join(parts)
    headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(body)))]
    for name, value in req.queryvars.items():
        if name.startswith('header-'):
            header_name = name[len('header-'):]
            headers.append((header_name, value))
    start_response(status, headers)
    return [body]

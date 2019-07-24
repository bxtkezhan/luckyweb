import cgi
import os
import time
import mimetypes
from wsgiref.headers import Headers
import json
from wsgiref.simple_server import make_server
from http.cookies import SimpleCookie


def notfound_404(environ, start_response):
    start_response('404 Not Found', [ ('Content-type', 'text/plain; charset=UTF-8') ])
    return [b'404 Not Found']

class StaticHandle:
    def __init__(self, static_dirs=None, block_size=16 * 4096, charset='UTF-8'):
        if static_dirs is None:
            static_dirs = [os.path.join(os.path.abspath('.'), 'static')]
        self.static_dirs = static_dirs
        self.charset = charset
        self.block_size = block_size

    # Search File
    def search_file(self, relative_file_path, dirs):
        print(relative_file_path)
        for d in dirs:
            if not os.path.isabs(d):
                d = os.path.abspath(d) + os.sep

            file_path = os.path.join(d, relative_file_path)
            if os.path.isfile(file_path) and os.access(file_path, os.R_OK):
                return file_path

    # Header utils
    def get_content_length(self, filename):
        stats = os.stat(filename)
        return str(stats.st_size)

    def generate_last_modified(self):
        # last_modified = time.strftime("%a, %d %b %Y %H:%M:%sS GMT", time.gmtime())
        last_modified = time.strftime("%a, %d %b %Y %T GMT", time.gmtime())
        return last_modified

    def get_content_type(self, mimetype, charset):
        if mimetype.startswith('text/') or mimetype == 'application/javascript':
            mimetype += '; charset={}'.format(charset)
        return mimetype

    # Response body iterator
    def _iter_and_close(self, file_obj, block_size, charset):
        """Yield file contents by block then close the file."""
        while True:
            try:
                block = file_obj.read(block_size)
                if block:
                    if isinstance(block, bytes):
                        yield block
                    else:
                        yield block.encode(charset)
                else:
                    raise StopIteration
            except StopIteration:
                file_obj.close()
                break

    def _get_body(self, filename, method, block_size, charset):
        if method == 'HEAD':
            return [b'']
        return self._iter_and_close(open(filename, 'rb'), block_size, charset)

    # View functions
    def static_file_view(self, environ, start_response, filename, block_size, charset):
        method = environ['REQUEST_METHOD'].upper()
        if method not in ('HEAD', 'GET'):
            start_response('405 METHOD NOT ALLOWED',
                           [('Content-Type', 'text/plain; charset=UTF-8')])
            return [b'']

        mimetype, encoding = mimetypes.guess_type(filename)
        headers = Headers([])
        headers.add_header('Content-Encodings', encoding)
        headers.add_header('Content-Type', self.get_content_type(mimetype, charset))
        headers.add_header('Content-Length', self.get_content_length(filename))
        headers.add_header('Last-Modified', self.generate_last_modified())
        headers.add_header("Accept-Ranges", "bytes")

        start_response('200 OK', headers.items())
        return self._get_body(filename, method, block_size, charset)

    def __call__(self, environ, start_response, filename):
        abs_file_path = self.search_file(filename, self.static_dirs)
        if abs_file_path:
            return self.static_file_view(environ, start_response, abs_file_path,
                                    self.block_size, self.charset)
        else:
            return notfound_404(environ, start_response)

class Cookie(SimpleCookie):
    def get_value(self, key):
        return self.get(key).value

    def output(self, header='Set-Cookie'):
        return (header, super(Cookie, self).output(header='').strip())

class Request:
    def __init__(self, environ):
        self.environ = environ
        self.params = self.environ.get('params')
        self.data = self.environ.get('data')
        self.method = self.environ.get('REQUEST_METHOD')
        self.cookie = Cookie(self.environ.get('HTTP_COOKIE', ''))

class Response:
    def __init__(self, start_response, charset):
        self.start_response = start_response
        self.charset = charset
        self.content_type = 'text/html; charset={}'.format(self.charset)
        self.set_cookie = Cookie()
        self.started = False

    def set_content_type(self, content_type):
        self.content_type = '{}; charset={}'.format(content_type, self.charset)

    def plain(self, obj):
        self.content_type = 'text/plain; charset={}'.format(self.charset)
        return obj

    def jsonify(self, obj, ensure_ascii=True, indent=None, sort_keys=False):
        self.content_type = 'application/json; charset={}'.format(self.charset)
        return json.dumps(obj, ensure_ascii=ensure_ascii, indent=indent, sort_keys=sort_keys)

    def start(self):
        if not self.started:
            self.start_response('200 OK', [('Content-type', self.content_type), self.set_cookie.output()])
            self.started = True
            return True
        return False

    def redirect(self, location):
        self.start_response('302 Found', [('Location', location), self.set_cookie.output()])
        self.started = True
        return '1'

class DocumentHandle:
    def __init__(self, function, charset):
        self.func = function
        self.charset = charset

    def __call__(self, environ, start_response):
        request = Request(environ)
        response = Response(start_response, self.charset)
        dumps = self.func(request, response)
        response.start()
        if hasattr(dumps, 'encode'):
            dumps = dumps.encode()
        yield dumps

class Server:
    def __init__(self, static_root='static', static_dirs=None,
                 block_size=16 * 4096, charset='UTF-8'):
        '''
        Arguments:
        - static_root: static path root for url, default static
        - static_dirs: truth static files direct directory
        - block_size: static file load block size, default 16 * 4096
        - charset: default utf-8
        '''
        self.pathmap = { }
        self.static_root = static_root.lstrip('/').rstrip('/')
        self.charset = charset
        self.pathmap[self.static_root] = StaticHandle(
                static_dirs, block_size, self.charset)

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO'].lstrip('/')
        if path.startswith(self.static_root):
            relative_file_path = '/'.join(path.split('/')[1:])
            return self.pathmap[self.static_root](environ, start_response, relative_file_path)

        params = cgi.FieldStorage(environ['wsgi.input'], environ=environ)
        method = environ['REQUEST_METHOD'].lower()
        environ['params'] = {}
        environ['data'] = {}
        for key in params:
            environ['params'][key] = params.getvalue(key)
            environ['data'][key] = params[key]
        handler = self.pathmap.get((method, '/' + path), notfound_404)
        return handler(environ, start_response)

    def register(self, path, function, methods=['GET']):
        for method in methods:
            self.pathmap[method.lower(), path] = DocumentHandle(function, self.charset)
        return function

    def run(self, host='127.0.0.1', port=8000):
        httpd = make_server(host, port, self)
        print('Running on http://{}:{}/ (Press CTRL+C to quit)'.format(
             {'0.0.0.0': '127.0.0.1'}.get(host, host), port))
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print('\nServer closed.')

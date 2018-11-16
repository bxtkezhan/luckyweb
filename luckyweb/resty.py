import cgi
import os
import time
import mimetypes
from wsgiref.headers import Headers


# Search File
def is_accessible(abs_file_path):
    return (
        os.path.exists(abs_file_path) and
        os.path.isfile(abs_file_path) and
        os.access(abs_file_path, os.R_OK)
    )

def search_file(relative_file_path, dirs):
    for d in dirs:
        if not os.path.isabs(d):
            d = os.path.abspath(d) + os.sep

        file = os.path.join(d, relative_file_path)
        if is_accessible(file):
            return file

# Header utils
def get_content_length(filename):
    stats = os.stat(filename)
    return str(stats.st_size)

def generate_last_modified():
    last_modified = time.strftime("%a, %d %b %Y %H:%M:%sS GMT", time.gmtime())
    return last_modified

def get_content_type(mimetype, charset):
    if mimetype.startswith('text/') or mimetype == 'application/javascript':
        mimetype += '; charset={}'.format(charset)
    return mimetype

# Response body iterator
def _iter_and_close(file_obj, block_size, charset):
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

def _get_body(filename, method, block_size, charset):
    if method == 'HEAD':
        return [b'']
    return _iter_and_close(open(filename, 'rb'), block_size, charset)

# View functions
def static_file_view(env, start_response, filename, block_size, charset):
    method = env['REQUEST_METHOD'].upper()
    if method not in ('HEAD', 'GET'):
        start_response('405 METHOD NOT ALLOWED',
                       [('Content-Type', 'text/plain; UTF-8')])
        return [b'']

    mimetype, encoding = mimetypes.guess_type(filename)
    headers = Headers([])
    headers.add_header('Content-Encodings', encoding)
    headers.add_header('Content-Type', get_content_type(mimetype, charset))
    headers.add_header('Content-Length', get_content_length(filename))
    headers.add_header('Last-Modified', generate_last_modified())
    headers.add_header("Accept-Ranges", "bytes")

    start_response('200 OK', headers.items())
    return _get_body(filename, method, block_size, charset)

def notfound_404(environ, start_response):
    start_response('404 Not Found', [ ('Content-type', 'text/plain; charset=utf-8') ])
    return [b'404 Not Found']

class PathDispatcher:
    def __init__(self, static_root='static', static_dirs=None,
                 block_size=16 * 4096, charset='UTF-8'):
        self.pathmap = { }
        self.static_root = static_root.lstrip('/').rstrip('/')
        if static_dirs is None:
            static_dirs = [os.path.join(os.path.abspath('.'), 'static')]
        self.static_dirs = static_dirs
        self.charset = charset
        self.block_size = block_size

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO'].lstrip('/')
        if path.startswith(self.static_root):
            relative_file_path = '/'.join(path.split('/')[1:])
            return self.static_handle(environ, start_response, relative_file_path)

        params = cgi.FieldStorage(environ['wsgi.input'],
                                  environ=environ)
        method = environ['REQUEST_METHOD'].lower()
        environ['params'] = { key: params.getvalue(key) for key in params }
        handler = self.pathmap.get((method, '/' + path), notfound_404)
        return handler(environ, start_response)

    def register(self, method, path, function):
        self.pathmap[method.lower(), path] = function
        return function

    def static_handle(self, environ, start_response, filename):
        abs_file_path = search_file(filename, self.static_dirs)
        if abs_file_path:
            return static_file_view(environ, start_response, abs_file_path,
                                    self.block_size, self.charset)
        else:
            return notfound_404(environ, start_response)

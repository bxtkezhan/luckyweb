import cgi
import os
import time
import mimetypes
from wsgiref.headers import Headers


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
                           [('Content-Type', 'text/plain; UTF-8')])
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

class DocumentHandle:
    def __init__(self, function, content_type):
        self.func = function
        self.content_type = content_type

    def __call__(self, environ, start_response):
        start_response('200 OK', [('Content-type', self.content_type)])
        dumps = self.func(environ, start_response)
        if hasattr(dumps, 'encode'):
            dumps = dumps.encode()
        yield dumps

class PathDispatcher:
    def __init__(self, static_root='static', static_dirs=None,
                 block_size=16 * 4096, charset='UTF-8'):
        self.pathmap = { }
        self.static_root = static_root.lstrip('/').rstrip('/')
        self.pathmap[self.static_root] = StaticHandle(
                static_dirs, block_size, charset)

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO'].lstrip('/')
        if path.startswith(self.static_root):
            relative_file_path = '/'.join(path.split('/')[1:])
            return self.pathmap[self.static_root](environ, start_response, relative_file_path)

        params = cgi.FieldStorage(environ['wsgi.input'], environ=environ)
        method = environ['REQUEST_METHOD'].lower()
        environ['params'] = {key: params.getvalue(key) for key in params}
        handler = self.pathmap.get((method, '/' + path), notfound_404)
        return handler(environ, start_response)

    def register(self, method, path, function, content_type='text/html'):
        self.pathmap[method.lower(), path] = DocumentHandle(function, content_type)
        return function

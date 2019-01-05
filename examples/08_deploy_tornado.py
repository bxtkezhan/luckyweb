from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

import luckyweb.blocks as B
from luckyweb import LuckyWeb


def helloserver(request, response):
    if request.method == 'POST':
        return response.jsonify(request.params)

    html = B.HtmlBlock(title='luckyweb deploy')
    grid = B.GridBlock([4, 4, 4])
    form = B.FormBlock('/', method='post', groups=[
        {'label': 'Name', 'type': 'text', 'placeholder': 'please input name text', 'name': 'name'},
        {'label': 'Email', 'type': 'email', 'placeholder': 'please input email', 'name': 'email'},
        {'label': 'Password', 'type': 'password', 'placeholder': 'please input password', 'name': 'password'}])
    html(
        grid(['', form, '']),
    )

    return html

app = LuckyWeb()
app.register('/', helloserver, methods=['GET', 'POST'])

if __name__ == '__main__':
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(8000, address='0.0.0.0')
    IOLoop.instance().start()

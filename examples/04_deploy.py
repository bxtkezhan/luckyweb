from gevent.pywsgi import WSGIServer
from multiprocessing import cpu_count, Process
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

server = WSGIServer(('', 8000), app, log=None)
server.start()

def serve_forever():
    server.start_accepting()
    server._stop_event.wait()

if __name__ == '__main__':
    for i in range(cpu_count()):
        p = Process(target=serve_forever)
        p.start()

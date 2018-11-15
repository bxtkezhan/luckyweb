import blocks as B


def hello_world(environ, start_response):
    start_response('200 OK', [ ('Content-type','text/html')])
    params = environ['params']

    html = B.HtmlBlock(title='Hello LuckyWeb powered by msdl_kk')
    navbar = B.NavbarBlock([
        {'href': '#', 'text': 'Lucky Web'},
        {'href': '#', 'text': 'Home', 'active': True},
        {'href': '#', 'text': 'Article'},
        {'href': '#', 'text': 'About'}
    ])
    container_img = B.ContainerBlock(cols_num=[2, 4, 2, 4], py=5)
    img = B.ImgBlock(src='https://www.python.org/static/img/python-logo.png', href='https://www.python.org')
    container_txt = B.ContainerBlock([3] * 4)

    html([
        navbar,
        container_img( 
            [img, img, img, img]
        ),
        container_img,
        container_img,
        container_img,
        container_txt(['<h3> {} </h3>'.format(params.get('name') or '')] * 4) ,
    ])

    yield html.encode('utf-8')

if __name__ == '__main__':
    from resty import PathDispatcher
    from wsgiref.simple_server import make_server

    dispatcher = PathDispatcher()
    dispatcher.register('GET', '/', hello_world)

    # Launch a basic server
    httpd = make_server('', 8080, dispatcher)
    print('Serving on port 8080...')
    httpd.serve_forever()

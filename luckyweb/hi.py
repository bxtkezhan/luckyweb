import blocks as B


def hello_world(environ, start_response):
    start_response('200 OK', [ ('Content-type','text/html')])
    params = environ['params']

    html = B.HtmlBlock(title='Hello LuckyWeb powered by msdl_kk')
    navbar = B.NavbarBlock(
        li_list=[
            {'href': '#', 'text': 'Lucky Web'},
            {'href': '#', 'text': 'Home', 'active': True},
            {'href': '#', 'text': 'Article'},
        ],
        ri_list=[
            {'href': '#', 'text': 'About'},
            {'href': '#', 'text': 'Contact us', 'btn': True},
        ]
    )
    grid_img = B.GridBlock(cols_num=[2, 4, 2, 4], py=5)
    img = B.ImgBlock(src='/static/L.png', href='https://github.com/bxtkezhan')
    grid_txt = B.GridBlock([3, 3, 3, 3], py=2)
    head = B.HeadingBlock(params.get('name') or '', head_num=1, display_num=3)
    grid_img_txt = B.GridBlock([2] * 6, py=3)

    html([
        navbar,
        grid_img( 
            [img, img, img, img]
        ),
        grid_txt(
            [head, head, head, head]
        ),
        grid_img_txt(
            [img + head] * 6,
        ),
    ])

    yield html.encode('utf-8')

if __name__ == '__main__':
    from resty import PathDispatcher
    from wsgiref.simple_server import make_server
    import os

    dispatcher = PathDispatcher()
    dispatcher.register('GET', '/', hello_world)

    # Launch a basic server
    httpd = make_server('', 8000, dispatcher)
    print('Serving on port 8000...')
    httpd.serve_forever()

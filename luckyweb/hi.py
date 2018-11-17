import blocks as B


def hello_world(environ, start_response):
    start_response('200 OK', [('Content-type','text/html')])
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
    head_img = B.HeadingBlock('Images', head_num=1, display_num=4)
    grid_img = B.GridBlock(cols_num=[2, 4, 2, 4], py=5)
    img = B.ImgBlock(src='/static/L.png', href='https://github.com/bxtkezhan')
    head_article = B.HeadingBlock('Article', head_num=1, display_num=4)
    grid_article = B.GridBlock([2] * 6, py=5)
    article = B.PBlock('Hello LuckWeb ... inputs: {}'.format(params.get('name') or ''))

    html([
        navbar,
        head_img,
        grid_img( 
            [img, img, img, img]),
        head_article,
        grid_article(
            [img + article] * 6),
    ])

    yield html.encode('UTF-8')

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

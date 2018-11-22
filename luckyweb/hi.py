import blocks as B


def hello_world(environ, start_response):
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
    head_img = B.HeadBlock('Images', head_num=1, display_num=4, center=True)
    grid_img = B.GridBlock(cols_num=[2, 4, 2, 4], py=5)
    img = B.ImgBlock(src='/static/L.png', href='https://github.com/bxtkezhan')
    head_article = B.HeadBlock('Article', head_num=1, display_num=4, center=True)
    grid_article = B.GridBlock([2] * 6, py=5)
    article = B.PBlock('Hello LuckWeb ... inputs: {}'.format(params.get('name') or ''))
    head_table = B.HeadBlock('Tables', head_num=1, display_num=4, center=True)
    grid_table = B.GridBlock([3] * 4, py=5)
    table = B.TableBlock(_class="table-striped table-dark", array=[
        ['#', 'Name', 'Email'],
        ['0', 'KK', 'K@gmail.com'],
        ['1', 'LL', 'L@gmail.com']])
    pages = B.PaginationBlock(pages=[
        {'href': '#', 'text': 'Prev'},
        {'href': '#', 'text': 1, 'active': True},
        {'href': '#', 'text': 2},
        {'href': '#', 'text': 3},
        {'href': '#', 'text': 4},
        {'href': '#', 'text': 'Next'}])

    html([
        navbar,
        head_img,
        grid_img( 
            [img, img, img, img]),
        head_article,
        grid_article(
            [img + article] * 6),
        head_table,
        grid_table(
            [table + pages] * 4),
    ])

    return html

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

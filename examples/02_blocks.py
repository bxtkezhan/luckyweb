import luckyweb.blocks as B


def helloblocks(request, response):
    html = B.HtmlBlock(title='Hello lucky blocks')

    navbar = B.NavbarBlock(
        left_items=[
            {'href': '/', 'text': 'Lucky Web'},
            {'href': '/', 'text': 'Home', 'active': True},
            {'href': '#', 'text': 'Article'},
        ],
        right_items=[
            {'href': '#', 'text': 'About'},
            {'href': '#', 'text': 'Contact us', 'btn': True},
        ]
    )

    head_p = B.HeadBlock('PBlock')
    p = B.PBlock('1234567890qwertyuiop ... zxcvbnm')

    head_img = B.HeadBlock('ImgBlock')
    img = B.ImgBlock(src='https://avatars0.githubusercontent.com/u/20847355?s=460&v=4')

    head_a = B.HeadBlock('ABlock')
    a = B.ABlock('luckyweb github repository', href='https://github.com/bxtkezhan/luckyweb')

    head_list = B.HeadBlock('ListBlock', center=True)
    _list = B.ListBlock([
        dict(href='#', text='aaaaaaaaaaaaaaaaaa'),
        dict(href='#', text='bbbbbbbbbbbbbbbbbb'),
        dict(href='#', text='cccccccccccccccccc')])

    head_table = B.HeadBlock('TableBlock', center=True)
    table = B.TableBlock([
        ['#', 'column 1', 'column 2', 'column 3', 'column 4', 'column 5'],
        ['1', '5.2', '4.1', '1.5', '0.1', 'setosa'],
        ['2', '6.0', '2.2', '4.0', '1.0', 'versicolor'],
        ['3', '4.9', '2.5', '4.5', '1.7', 'virginica']])

    head_form = B.HeadBlock('FormBlock', center=True)
    form = B.FormBlock(action='/', groups=[
        {'label': 'Username', 'type': 'text', 'placeholder': 'input username', 'name': 'username'},
        {'label': 'Password', 'type': 'password', 'placeholder': 'input password', 'name': 'password'}])

    head_card = B.HeadBlock('CardBlock', center=True)
    card = B.CardBlock('Card header')

    head_grid = B.HeadBlock('GridBlock', center=True)
    grid = B.GridBlock([4, 4, 4])

    html([
        navbar,
        head_p,
        p,
        '<br><hr color="#F00">',
        head_img,
        img,
        '<br><hr color="#F00">',
        head_a,
        a,
        '<br><hr color="#F00">',
        head_list,
        _list,
        '<br><hr color="#F00">',
        head_table,
        table,
        '<br><hr color="#F00">',
        head_form,
        form,
        '<br><hr color="#F00">',
        head_card,
        card([
            p,
            img,
            a]),
        '<br><hr color="#F00">',
        head_grid,
        grid([_list, table, form])
    ])

    return html

if __name__ == '__main__':
    from luckyweb import LuckyWeb

    app = LuckyWeb()
    app.register('/', helloblocks)
    app.run()

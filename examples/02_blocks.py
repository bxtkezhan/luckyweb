import luckyweb.blocks as B


def helloblocks(request, response):
    params = request.params

    html = B.HtmlBlock(title='Hello lucky blocks')
    navbar = B.NavbarBlock(
        li_list=[
            {'href': '/', 'text': 'Lucky Web'},
            {'href': '/', 'text': 'Home', 'active': True},
            {'href': '#', 'text': 'Article'},
        ],
        ri_list=[
            {'href': '#', 'text': 'About'},
            {'href': '#', 'text': 'Contact us', 'btn': True},
        ]
    )

    grid_1 = B.GridBlock([1, 3, 7, 1])
    img = B.ImgBlock('/static/L.png', href='https://github.com/bxtkezhan/luckyweb', _class='')
    head_1 = B.HeadBlock('<center> 莎士比亚十四行诗 </center>')
    lis = B.ListBlock([
        {'href': '#', 'text': 'Let me not to the marriage of true minds - 我绝不承认两颗真心的结合'},
        {'href': '#', 'text': 'Admit impediments. Love is not love - 有任何障碍。这样的爱不是真爱'},
        {'href': '#', 'text': 'Which alters when it alteration finds, - 若是遇有变节的机会就改变，'},
        {'href': '#', 'text': 'Or bends with the remover to remove: - 或是被强势剥离就屈服：'},
        {'href': '#', 'text': 'O, no! it is an ever-fix`ed mark, 哦，- 那不是爱！爱是坚定的烽火，'}])

    grid_2 = B.GridBlock([6, 6])
    card = B.CardBlock('La La La !!!')
    head_2 = B.HeadBlock('<center> IRIS Table </center>', head_num=4)
    table = B.TableBlock([
        ['#', '花萼长度', '花萼宽度', '花瓣长度', '花瓣宽度', '属种'],
        ['1', '5.2', '4.1', '1.5', '0.1', 'setosa'],
        ['2', '6.0', '2.2', '4.0', '1.0', 'versicolor'],
        ['3', '4.9', '2.5', '4.5', '1.7', 'virginica']])

    html([
        navbar,
        grid_1(
            ['', img, head_1 + lis, '']),
        grid_2(
            [card(head_2 + table)] * 2),
    ])

    return html

if __name__ == '__main__':
    from luckyweb import LuckyWeb

    app = LuckyWeb()
    app.register('/', helloblocks)
    app.run()

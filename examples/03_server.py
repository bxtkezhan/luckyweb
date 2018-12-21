import luckyweb.blocks as B


def helloserver(request, response):
    if request.method == 'POST':
        return response.jsonify(request.params)

    html = B.HtmlBlock(title='Hello lucky server')
    grid = B.GridBlock([4, 4, 4])
    form = B.FormBlock('/', method='post', groups=[
        {'label': 'Name', 'type': 'text', 'placeholder': 'please input name text', 'name': 'name'},
        {'label': 'Email', 'type': 'email', 'placeholder': 'please input email', 'name': 'email'},
        {'label': 'Password', 'type': 'password', 'placeholder': 'please input password', 'name': 'password'}])
    img = B.ImgBlock(src='/static/L.png')

    html(
        grid(['', form, img]),
    )

    return html

if __name__ == '__main__':
    from luckyweb import LuckyWeb

    app = LuckyWeb()
    app.register('/', helloserver, methods=['GET', 'POST'])
    app.run(host='localhost', port=5000)

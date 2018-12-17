import luckyweb.blocks as B


def helloserver(request, response):
    if request.method == 'POST':
        script = request.params.get('file', b'').decode()
        return response.plain(script)

    html = B.HtmlBlock(title='Upload file')
    grid = B.GridBlock([4, 4, 4])
    form = B.FormBlock('/', method='post', groups=[
        {'label': 'Select text file', 'type': 'file', 'name': 'file'}])
    html(
        grid(['', form, '']),
    )

    print(request.environ.get('userfile'))

    return html

if __name__ == '__main__':
    from luckyweb import LuckyWeb

    app = LuckyWeb()
    app.register('/', helloserver, methods=['GET', 'POST'])
    app.run(host='localhost', post=5000)

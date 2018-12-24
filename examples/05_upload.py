import luckyweb.blocks as B


def helloserver(request, response):
    if request.method == 'POST':
        filedata = request.data.get('file')
        filename = filedata.filename
        filetype = filedata.type
        content = filedata.file.read().decode()
        result = '# filename: {}, type: {}\n\n{}'.format(filename, filetype, content)
        return response.plain(result)

    html = B.HtmlBlock(title='Upload file')
    grid = B.GridBlock([4, 4, 4])
    form = B.FormBlock('/', method='post', groups=[
        {'label': 'Select text file', 'type': 'file', 'name': 'file'}])
    html(
        grid(['', form, '']),
    )

    return html

if __name__ == '__main__':
    from luckyweb import LuckyWeb

    app = LuckyWeb()
    app.register('/', helloserver, methods=['GET', 'POST'])
    app.run()

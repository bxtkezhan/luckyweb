import luckyweb.blocks as B


def helloserver(request, response):
    if request.method == 'POST':
        location = request.params.get('location') or 'https://www.python.org'
        return response.redirect(location)

    html = B.HtmlBlock(title='Redirect')
    grid = B.GridBlock([4, 4, 4])
    form = B.FormBlock('/', method='post', groups=[
        {'label': 'Location', 'placeholder': 'input a location, default www.python.org', 'type': 'text', 'name': 'location'}])
    html(
        grid(['', form, '']),
    )

    return html

if __name__ == '__main__':
    from luckyweb import LuckyWeb

    app = LuckyWeb()
    app.register('/', helloserver, methods=['GET', 'POST'])
    app.run()

import luckyweb.blocks as B
import json


def cookie_dumps(cookie):
    result = {}
    for key in cookie.keys():
        result[key] = cookie.get_value(key)
    return json.dumps(result, indent=2)

def mycookie(request, response):
    if request.method == 'POST':
        cooke_key = request.params.get('cooke_key') or 'default'
        cooke_value = request.params.get('cooke_value') or 'default'
        response.set_cookie[cooke_key] = cooke_value
        return response.redirect('/')

    html = B.HtmlBlock(title='My cookie')
    grid = B.GridBlock([2, 4, 4, 2])
    form = B.FormBlock(action='/', groups=[
        dict(label='Cookie Key:', type='text', placeholder='please input key', name='cooke_key'),
        dict(label='Cookie Value:', type='text', placeholder='please input value', name='cooke_value')])
    view = B.HeadBlock('Request cookie:', center=True) 
    view += '<pre>\n{}\n</pre>'.format(cookie_dumps(request.cookie))

    html([
        grid(['', form, view, '']),
    ])
    return html

if __name__ == '__main__':
    from luckyweb import LuckyWeb

    app = LuckyWeb()
    app.register('/', mycookie, methods=['GET', 'POST'])
    app.run()

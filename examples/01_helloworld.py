def helloworld(request, response):
    return '<h1> Hello {} </h1>'.format(request.environ.get('REMOTE_ADDR'))

if __name__ == '__main__':
    from luckyweb import LuckyWeb

    app = LuckyWeb()
    app.register('/', helloworld)
    app.run(host='0.0.0.0')

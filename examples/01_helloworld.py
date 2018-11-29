def helloworld(request, response):
    return '<h1> Hello world </h1>'

if __name__ == '__main__':
    from luckyweb import LuckyWeb

    app = LuckyWeb()
    app.register('/', helloworld)
    app.run()

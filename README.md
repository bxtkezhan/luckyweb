# luckyweb
> 一款可以开心的创建Web App的工具

luckyweb是一款简单明了的开源Python Web开发框架，不依赖第三方包，同时内置blocks组件可以快速生成前端UI，让开发者集中精力与后端开发。

**安装方法**

1 . 直接下载项目[master.zip](https://github.com/bxtkezhan/luckyweb/archive/master.zip)，在本地构建安装

```bash
cd luckyweb-master/
python3 setup.py build
python3 setup.py install
```

2 . 使用git客户端克隆到本地，然后构建安装

```bash
git clone https://github.com/bxtkezhan/luckyweb.git
cd luckyweb/
python3 setup.py build
python3 setup.py install
```

3 . 使用`pip`工具直接clone并安装

```bash
pip install git+https://github.com/bxtkezhan/luckyweb.git
```

**Hello World**

```python
# hello.py
# run: python3 hello.py
def helloworld(request, response):
    return '<h1> Hello world </h1>'

if __name__ == '__main__':
    from luckyweb import LuckyWeb

    app = LuckyWeb()
    app.register('/', helloworld)
    app.run()
```
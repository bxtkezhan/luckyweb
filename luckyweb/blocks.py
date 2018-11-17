from jinja2 import Template
import collections
import os

LUCKY_HOME = os.path.dirname(os.path.abspath(__file__))
LUCKY_TEMPLATES = os.path.join(LUCKY_HOME, 'templates')

def load_template(filename):
    tpl_path = os.path.join(LUCKY_TEMPLATES, filename)
    with open(tpl_path) as f:
        tpl_str = f.read()
    return Template(tpl_str)

class BaseBlock:
    def __init__(self, tpl_filename):
        self.template = load_template(tpl_filename)
        self.args = {}
        self.html = ''

    def __call__(self, variable=None):
        if variable is not None:
            if isinstance(variable, str) or (not isinstance(variable, collections.Iterable)):
                variable = [variable]
            self.args.update({'variable': variable})
            self.html = self.template.render(args=self.args)
        return self.html

    def __repr__(self):
        return self.html

    def __add__(self, obj):
        return self.html + '\n' + str(obj)

    def encode(self, encoding='utf-8'):
        return self.html.encode(encoding)

class HtmlBlock(BaseBlock):
    def __init__(self, title=''):
        super(HtmlBlock, self).__init__('html.tpl')
        self.args.update({'title': title})

class GridBlock(BaseBlock):
    def __init__(self, cols_num=[], py=5):
        super(GridBlock, self).__init__('grid.tpl')
        self.args.update({'cols_num': cols_num, 'py': py})

class NavbarBlock(BaseBlock):
    def __init__(self, li_list=[], ri_list=[]):
        super(NavbarBlock, self).__init__('navbar.tpl')
        self.args.update({'li_list': li_list, 'ri_list': ri_list})
        self.html = self.template.render(args=self.args)

class ImgBlock(BaseBlock):
    def __init__(self, src, href='#', alt='#'):
        super(ImgBlock, self).__init__('img.tpl')
        self.args.update({
            'src': src, 'href': href, 'alt': alt})
        self.html = self.template.render(args=self.args)

class HeadingBlock(BaseBlock):
    def __init__(self, text, head_num=3, display_num=None):
        super(HeadingBlock, self).__init__('heading.tpl')
        self.args.update({
            'text': text, 'head_num': head_num, 'display_num': display_num})
        self.html = self.template.render(args=self.args)

class PBlock(BaseBlock):
    def __init__(self, text, lead=False):
        super(PBlock, self).__init__('p.tpl')
        self.args.update({'text': text, 'lead': lead})
        self.html = self.template.render(args=self.args)

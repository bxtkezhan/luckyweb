from setuptools import setup, find_packages

with open('luckyweb/version.py') as f:
    version_script = f.read()
    exec(version_script)

setup(
    name='luckyweb',
    version=__version__,
    author='bxtkezhan-kk',
    author_email='bxtkezhan@gmail.com',
    description='web framework for python3',
    url='https://bxtkezhan.github.io/luckyweb',
    license='MIT License',
    keywords='lucky web',
    packages=find_packages(),
    package_data={'luckyweb':[
        'templates/*.tpl'
    ]}
)

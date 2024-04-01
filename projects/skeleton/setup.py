try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'descriptin': 'My Journey to Software Engineer',
    'author': 'Chris Jin',
    'url': 'https://github.com/fscj-4raxhel/my-journey-to-learn-python3-the-hard-way',
    'download_url': 'https://github.com/fscj-4raxhel/my-journey-to-learn-python3-the-hard-way',
    'author_email': 'My email',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'learn-python-the-hard-way'
}

setup(**config)
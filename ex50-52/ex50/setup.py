try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'My project',
	'author': 'My name',
	'url': 'URL to get it at',
	'download_url': 'where to download it',
	'author_email': 'my email',
	'version': '0.1'
	'install_requires': ['nose'],
	'packages': ['ex50'],
	'scripts': [],
	'name': 'project name'
}

setup(**config)

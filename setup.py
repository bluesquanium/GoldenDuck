from setuptools import setup

packages = \
['goldenduck',
 'goldenduck.pkg']

package_data = \
{'': ['*']}

install_requires = \
['pyyaml>=5.3,<6.0']

setup_kwargs = {
    'name': 'goldenduck',
    'version': '0.1.0',
    'description': 'Golden Duck - Crawl Stock Data & Visualize',
    'long_description': 'edit this later',
    'long_description_content_type': 'text/markdown',
    'author': 'Bluesquanium',
    'author_email': 'bluesquanium@gmail.com',
    'maintainer': 'Bluesquanium',
    'maintainer_email': 'bluesquanium@gmail.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}

setup(**setup_kwargs)
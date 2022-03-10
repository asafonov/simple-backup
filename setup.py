try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from simple.version import version

config = {
    'description': 'simple-backup - Simple backup server',
    'version': version,
    'packages': ['simple'],
    'scripts': [],
    'name': 'spass',
    'entry_points': {
        'console_scripts': [
            'simple-backup = simple.__main__:main'
        ]
    },
}

setup(**config)

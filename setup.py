"""Setup file for absolute paths plugin"""
from setuptools import setup, find_packages

setup(
    name='mkdocs-absolute-paths-plugin',
    version='0.1.0',
    description='MkDocs plugin to convert relative URLs to absolute paths',
    py_modules=['absolute_paths_plugin'],
    install_requires=['mkdocs>=1.0.0'],
    entry_points={
        'mkdocs.plugins': [
            'absolute-paths = absolute_paths_plugin:AbsolutePathsPlugin',
        ]
    }
)

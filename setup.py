import os
from setuptools import setup, find_packages

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    long_description = 'Thumbor mongodb storage adapters'


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="tc_mongodb",
    version="5.2.4",
    author="Thumbor Community",
    description=("Thumbor thumbor storage adapters - France.tv Release"),
    license="MIT",
    keywords="thumbor mongodb mongo",
    url="https://github.com/francetv/mongodb",
    packages=[
        'tc_mongodb',
        'tc_mongodb.storages',
        'tc_mongodb.result_storages'
    ],
    long_description=long_description,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
    install_requires=[
        'thumbor>=6.5.0',
        'pymongo>=3.4.0'
    ]
)

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
    name="thumbor_mongodb_storage",
    version="5.2.5",
    author="Thumbor Community",
    description=("Thumbor thumbor storage adapters - France.tv Release"),
    license="MIT",
    keywords="thumbor mongodb mongo",
    url="https://github.com/francetv/mongodb",
    packages=[
        'thumbor_mongodb_storage',
        'thumbor_mongodb_storage.storages',
        'thumbor_mongodb_storage.result_storages'
    ],
    long_description=long_description,
    classifiers=[
        'Development Status ::4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
    install_requires=[
        'thumbor>=6.5.0',
        'pymongo>=3.4.0'
    ]
)

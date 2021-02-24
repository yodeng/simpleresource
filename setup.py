import os

from setuptools import setup
from src import __version__


def getdes():
    des = ""
    with open(os.path.join(os.getcwd(), "README.md")) as fi:
        des = fi.read()
    return des


setup(
    name="simpleresource",
    version=__version__,
    package_dir={"simpleresource": "src"},
    packages=['simpleresource'],
    author="Deng Yong",
    url="https://github.com/yodeng/simpleresource",
    long_description=getdes(),
    long_description_content_type='text/markdown',
    author_email="yodeng@tju.edu.cn",
    license="BSD",
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
)

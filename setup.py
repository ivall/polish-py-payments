from setuptools import setup, find_packages
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='polish-py-payments',
    version='1.0.0',
    author='ivall',
    description='Polish payment providers in python',
    long_description=long_description,
    url='https://github.com/ivall/polish-py-payments',
    keywords='polish payments, payments, payment provider',
    python_requires='>=3.6, <4',
    install_requires=['requests', 'hashlib'],
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    packages=find_packages()
)
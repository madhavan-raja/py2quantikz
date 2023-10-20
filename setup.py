from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Converts Quantum Circuit Code to quantikz Diagrams'

setup(
    name='py2quantikz',
    version=VERSION,
    author='Madhavan Raja',
    author_email='madhavanraja99@gmail.com',
    description=DESCRIPTION,
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
from setuptools import setup, find_packages

VERSION = '0.0.3'
DESCRIPTION = 'Converts Quantum Circuit Code to quantikz Diagrams'
LONG_DESCRIPTION = open('README.md').read()

setup(
    name='py2quantikz',
    version=VERSION,
    license='MIT',
    author='Madhavan Raja',
    author_email='madhavanraja99@gmail.com',
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    url='https://github.com/madhavan-raja/py2quantikz',
    packages=["py2quantikz"],
    keywords=['python', 'tikz', 'quantikz', 'latex', 'quantum'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
from setuptools import setup, find_packages

setup(
    name='py2quantikz',
    version='0.1.0',
    author='Madhavan Raja',
    author_email='madhavanraja99@gmail.com',
    description='Conveerts Quantum Circuit Code to quantikz Diagrams',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
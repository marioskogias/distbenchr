from setuptools import setup

setup(name='distbenchr',
        version='0.1',
        description='A library for running distributed benchmarks',
        author='Marios Kogias',
        author_email='marios.kogias@epfl.ch',
        license='MIT',
        packages=['distbenchr'],
        install_requires=[
            'fabric'
        ],
        zip_safe=False)

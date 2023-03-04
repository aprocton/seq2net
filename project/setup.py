from setuptools import setup
setup(
    name="seq2net",
    version="0.1",
    packages=["seq2net"],
    author="Alexander Procton",
    classifiers=["Programming Language :: Python :: 3"],
    install_requires=[
        'numpy',
        'pandas',
        'igraph',
    ],
)

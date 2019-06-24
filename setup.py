# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name='ta-modin',
    packages=['ta-modin'],
    version='0.4.6',
    description='Technical Analysis Library in Python',
    long_description='A Technical Analysis library for financial time series datasets, useful for feature engineering. It is built on Pandas (Modin for speedup).',
    author='Dario Lopez Padial (Bukosabino)',
    author_email='Bukosabino@gmail.com',
    url='https://github.com/bukosabino/ta',
    maintainer='Adam King (notadamking)',
    maintainer_email='adamjking3@gmail.com',
    install_requires=[
        'numpy',
        'pandas',
        'modin',
        'scikit-learn'
    ],
    download_url='https://github.com/notadamking/ta/tarball/0.4.6',
    keywords=['technical analysis', 'python3', 'pandas', 'modin'],
    license='The MIT License (MIT)',
    classifiers=[],
)

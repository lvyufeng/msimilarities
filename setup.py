# -*- coding: utf-8 -*-
import sys

from setuptools import setup, find_packages

# Avoids IDE errors, but actual version is read from version.py
__version__ = "0.0.1"

if sys.version_info < (3,):
    sys.exit('Sorry, Python3 is required.')

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='msimilarities',
    version=__version__,
    description='Similarities is a toolkit for compute similarity scores between two sets of strings.',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Lvyufeng',
    author_email='lvyufeng@cqu.edu.cn',
    url='https://github.com/lvyufeng/msimilarities',
    license="Apache License 2.0",
    zip_safe=False,
    python_requires=">=3.7.0",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    keywords='msimilarities,Chinese Text Similarity Calculation Tool,similarity,word2vec',
    install_requires=[
        "ms2vec",
        "jieba>=0.39",
        "loguru",
        "Pillow",
        "fire",
        "autofaiss",
        "mindnlp",
    ],
    packages=find_packages(),
)

from setuptools import setup, find_packages
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='tasqalent-shared',
    version='1.0.1',
    description='Shared utilities, types and helpers for TASQALENT (Python/Flask)',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Youssef Tawakal',
    author_email='youssef7931@gmail.com',
    url='https://github.com/tasqalent/tq-shared-python',
    packages=find_packages(),
    python_requires='>=3.8',
    install_requires=[
        # 'flask>=2.0.0'
    ],
    extras_require={
        'dev': [
            'pytest>=7.0.0',
            'black>=22.0.0',
            'flake8>=4.0.0'
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11'
    ]
)
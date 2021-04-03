"""setup.py for the script."""
from setuptools import setup, find_packages

setup(
    name='gitignore-cov',
    version='0.0.1',
    author='Andrey Nechaev',
    author_email='andrewnech@gmail.com',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['gitignore-cov = gitcov.main:main']
    },
)

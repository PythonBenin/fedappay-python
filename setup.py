import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

with open(os.path.join(os.path.dirname(__file__), 'LICENSE')) as copy_right:
    LICENSE = copy_right.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='fedapay',
    version='0.0.1',
    packages=[p for p in find_packages('.', exclude=['tests*'])],
    include_package_data=True,
    license=LICENSE,
    description='FedaPay API Python Package',
    long_description=README,
    url='https://github.com/sphinxxanxus',
    author='Corentin Allohoumbo',
    author_email='corentinalcoy@gmail.com',
    install_requires=[
        'requests==2.24.0',
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: Electronic Payment :: Web Development ',
    ],
)

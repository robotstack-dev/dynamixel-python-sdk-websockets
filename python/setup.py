
from setuptools import setup, find_packages
import platform

setup(
    name='dynamixelSDK_websockets',
    version='3.7.51.dev1',
    packages=['dynamixelSDK_websockets'],
    package_dir={'': 'src'},
    license='Apache 2.0',
    description='fork of DynamixelSDK python package with added websockets support',
    long_description=open('README.txt').read(),
    url='https://github.com/nsted/dyamixelSDK-websockets',
    author='Nicholas Stedman',
    author_email='nick@devicist.com',
    install_requires=[
        'pyserial',
        'websocket-client' 
    ]
)
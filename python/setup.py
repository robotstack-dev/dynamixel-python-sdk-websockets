
from setuptools import setup, find_packages
import platform

setup(
    name='dynamixel_sdk_with_websockets',
    version='3.7.51-dev1.0',
    packages=['dynamixel_sdk'],
    package_dir={'': 'src'},
    license='Apache 2.0',
    description='Dynamixel SDK 3 python package with custom modifications',
    long_description=open('README.txt').read(),
    url='https://github.com/nsted/DynamixelSDK-websocket',
    author='Leon Jung, Nicholas Stedman',
    author_email='nick@devicist.com',
    install_requires=[
        'pyserial',
        'websocket-client' 
    ]
)
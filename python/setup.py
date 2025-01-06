
from setuptools import setup, find_packages
import platform

setup(
    name='smart_servo_websockets',
    version='3.7.51.dev4',
    packages=['smart_servo_websockets'],
    package_dir={'': 'src'},
    license='Apache 2.0',
    description='Smart Servo Websockets python package forked from DynamixelSDK',
    long_description=open('README.txt').read(),
    url='https://github.com/nsted/smart-servo-websockets',
    author='Leon Jung, Nicholas Stedman',
    author_email='nick@devicist.com',
    install_requires=[
        'pyserial',
        'websocket-client' 
    ]
)
from setuptools import setup

setup(
    name='dynamixelSDK_websockets',
    version='0.0.3',
    packages=['dynamixelSDK_websockets'],
    package_dir={'': 'src'},
    description='Python SDK for Dynamixel with WebSocket support',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Nicholas Stedman',
    author_email='nick@robotstack.com',
    url='https://github.com/robotstack-dev/dynamixel-python-sdk-websockets',
    install_requires=[
        'pyserial>=3.0',
        'websocket-client>=1.8.0'
    ],
    python_requires='>=3.7',
    license='Apache-2.0',
)
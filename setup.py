from setuptools import setup, find_packages

setup(name='translatetool',
version='1.0.1',
description='A Papago Translate module.',
author='Jaewoo Lee',
author_email='jaewoolee82@kakao.com',
url='https://github.com/jaewoolee82/translatetool',
license='MIT',
py_modules=['translatetool'],
python_requires='>=3',
install_requires=['aiohttp'],
packages=['translatetool']
)
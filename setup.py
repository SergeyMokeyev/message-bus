from setuptools import setup, find_packages


setup(
    name='message-bus-redis',
    version='0.1.0',
    author='Sergey Mokeyev',
    author_email='sergey.mokeyev@gmail.com',
    description='Message bus between service by redis',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/SergeyMokeyev/message-bus-redis.git',
    data_files=[
        ('README.md', ['README.md'])
    ],
    package_dir={
        '': 'src'
    },
    packages=find_packages(where='src'),
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)'
    ],
    install_requires=[
        'aioredis'
    ]
)

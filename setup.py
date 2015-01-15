from distutils.core import setup

setup(
    name='appnexusclient',
    version='0.1.0',
    author='Emmanuel Job',
    author_email='emmanuel.job@accuenmedia.com',
    packages=['appnexusclient'],
    scripts=[],
    url='http://www.accuenmedia.com',
    license='LICENSE.txt',
    description='A simple client for the AppNexus console.',
    long_description=open('README.txt').read(),
    install_requires=[
        "requests",
    ],
)

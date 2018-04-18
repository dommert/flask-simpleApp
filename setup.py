# Flask-simpleApp 
# Version 1.0-alpha
# (C) 2018 - Abstergo Inc


from setuptools import setup

setup(
    name='yourapplication',
    packages=['yourapplication'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-sqlalchemy',
    ],
)
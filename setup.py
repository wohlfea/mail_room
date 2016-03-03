from setuptools import setup

setup(
    name='mail_room',
    description='A Python program to manage donation thank you emails',
    version=0.1,
    author='AJ Wohlfert and Kyle Richardson',
    license='MIT',
    py_modules=['mail_room'],
    packages_dir={'': 'src'},
    extras_require={'test': ['pytest', 'pytest-xdist', 'tox']}
)

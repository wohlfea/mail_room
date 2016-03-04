from setuptools import setup

setup(
    name='mail-room',
    description='A Python program to manage donation thank you emails',
    version=0.1,
    author='AJ Wohlfert and Kyle Richardson',
    license='MIT',
    py_modules=['mail_room'],
    package_dir={'': 'src'},
    install_requires=['future'],
    extras_require={'test': ['pytest', 'pytest-xdist', 'tox']},
    entry_points={
        'console_scripts': [
            "mailroom = mail_room:menu"
        ]
    }
)

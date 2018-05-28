from setuptools import setup, find_packages

setup(
    name='python-package-example',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='An example python package',
    install_requires=[],
    url='https://github.com/MiloszJurewicz/python_lab10',
    author='Milosz Jurewicz',
    author_email='myemail@example.com'
)
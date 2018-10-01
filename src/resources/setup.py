from setuptools import setup, find_packages

setup(
    name="uk-postalcode-validator",
    version="1.0.0",
    license="MIT",
    packages=find_packages(),
    install_requires=['nose2==0.8.0',
                      'pycodestyle==2.4.0'],
    description='UK Postcode Validator',
    long_description="\n" + open('README.md').read()
)

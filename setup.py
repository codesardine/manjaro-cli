from setuptools import setup, find_packages

setup(
    name='manjaro-cli',
    version='0.1',
    packages=["Manjaro.CLI"],
    package_dir={"": "src"},
    url='https://github.com/Manjaro-WebDad/libmanjaro.git',
    license='GPL',
    author='Vitor Lopes',
    description='Manjaro CLI'
)

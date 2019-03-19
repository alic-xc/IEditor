from setuptools import setup, find_packages

with open("README.md",'r') as fh:

    full_description = fh.read()


setup(
    name = 'IEditor By Alic',
    version = '1.0',
    author = 'alade olamilekan ismail',
    author_email = 'aladelekan187@gmail.com',
    long_description =  full_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alic-xc/ImageEditor",
    packages = find_packages(),
    classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],

)
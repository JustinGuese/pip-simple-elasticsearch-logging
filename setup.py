import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='simple-elastic-logging',  
    version='0.1',
    scripts=['simple-elastic-logging'] ,
    author="Justin Guese",
    author_email="guese.justin@gmail.com",
    description="A logger using Elasticsearch in the background with a focus on simplicity.",
    long_description=long_description,
long_description_content_type="text/markdown",
    url="https://github.com/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
 )
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='simpleelasticlogging',  
    version='0.0.5',
    author="Justin Guese",
    install_requires=['elasticsearch'],
    author_email="guese.justin@gmail.com",
    description="A logger using Elasticsearch in the background with a focus on simplicity.",
    long_description=long_description,
long_description_content_type="text/markdown",
    url="https://github.com/JustinGuese/pip-simple-elasticsearch-logging",
    packages=["simpleelasticlogging"],
    package_dir={"": "src"},
    # packages=setuptools.find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
 )
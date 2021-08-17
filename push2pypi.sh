#!/bin/bash
rm -rf build dist src/simpleelasticlogging.egg-info
python setup.py sdist
python setup.py bdist_wheel --universal
twine upload dist/*

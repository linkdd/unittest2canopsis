#!/bin/bash

virtualenv .
. ./bin/activate
pip install -r requirements.txt
python setup.py install

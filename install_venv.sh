#!/bin/bash
curl -O https://bootstrap.pypa.io/get-pip.py
python get-pip.py --user
pip install --user virtualenv
mkdir flask-app
cd flask-app
virtualenv
virtualenv --python=python2.7 flaskenv
source flaskenv/bin/activate
pip install flask
pip install requests
pip install tweepy
python server.py
pip freeze > requirements.txt

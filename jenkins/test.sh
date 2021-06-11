#!/bin/bash

sudo apt-get update
sudo apt-get install python3-venv python3-pip -y

python3 -m venv venv
source venv/bin/activate

pip3 install -r testing_requirements.txt

python3 -m pytest service1 --cov=application --cov-report term-missing
python3 -m pytest service2 --cov=app --cov-report term-missing
python3 -m pytest service3 --cov=app --cov-report term-missing
python3 -m pytest service4 --cov=app --cov-report term-missing
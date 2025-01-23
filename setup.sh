#!/bin/bash
#  install dependencies 
echo "Installing dependencies"	

pip install setuptools
pip install -r requirements.txt


# Run django commands 
echo "Running Django commands"
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic

# install tailwind dependencies
echo "Installing tailwind dependencies"
# python manage.py tailwind install
# python manage.py tailwind start
# Run the server
echo "Running the server"

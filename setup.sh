#!/bin/bash
#  install dependencies 
echo "Installing dependencies"	

pip install setuptools
pip install -r requirements.txt
pip install whitenoise



# Run django commands 
echo "Running Django commands"
python manage.py makemigrations
python manage.py migrate

# install tailwind dependencies
echo "Installing tailwind dependencies"
# python manage.py tailwind install
# python manage.py tailwind start
# Run the server
echo "Running the server"
# python manage.py collectstatic
python manage.py collectstatic --noinput

python manage.py runserver
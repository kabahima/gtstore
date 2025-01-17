#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e  

echo "Installing dependencies..."
pip install --upgrade pip
pip install setuptools
pip install -r requirements.txt

# Run Django commands
echo "Running Django database migrations..."
python manage.py makemigrations
python manage.py migrate

# Install Tailwind dependencies (uncomment if needed)
# echo "Installing Tailwind dependencies..."
# python manage.py tailwind install
# python manage.py tailwind start

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Setup completed successfully!"

#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# Install dependencies
echo "Installing dependencies"

pip install -r requirements.txt

# Run Django commands
echo "Running Django commands"
python manage.py makemigrations
python manage.py migrate

# Collect static files
echo "Collecting static files"
python manage.py collectstatic --noinput

echo "Setup complete."
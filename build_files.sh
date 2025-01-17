#!/bin/bash
# Exit on error
set -e

# Install dependencies
pip install -r requirements.txt

# Run Django commands
python manage.py makemigrations
python manage.py migrate

# Install Tailwind dependencies (uncomment if needed)
# python manage.py tailwind install
# python manage.py tailwind build

# Collect static files
python manage.py collectstatic --noinput

# Create a directory for the static files
mkdir -p staticfiles_build
mv staticfiles/* staticfiles_build/
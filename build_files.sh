#!/bin/bash
# Exit on error
set -e

# Check if Python3 and pip are installed, and install them if necessary
if ! command -v python3 &> /dev/null
then
    echo "Python3 could not be found. Installing..."
    apt-get update && apt-get install -y python3 python3-pip
fi

if ! command -v pip3 &> /dev/null
then
    echo "pip3 could not be found. Installing..."
    python3 -m ensurepip --upgrade
    python3 -m pip install --upgrade pip
fi

# Install dependencies from requirements.txt
pip3 install -r requirements.txt

# Run Django commands to apply migrations
python3 manage.py makemigrations
python3 manage.py migrate

# Install Tailwind dependencies (uncomment if you need to install and build Tailwind CSS)
# python3 manage.py tailwind install
# python3 manage.py tailwind build

# Collect static files
python3 manage.py collectstatic --noinput

# Create a directory for the static files
mkdir -p staticfiles_build
mv staticfiles/* staticfiles_build/

echo "Build completed successfully."

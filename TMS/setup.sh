<<<<<<< HEAD
#!/bin/bash

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install dependencies from requirements.txt
pip install -r requirements.txt


# Apply migrations
python manage.py makemigrations
python manage.py migrate

# Create a superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic --noinput

# Start the development server
python manage.py runserver


### If any permisssion issues use the command --> chmod with filename(setup.sh)
=======
#!/bin/bash

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install dependencies from requirements.txt
pip install -r requirements.txt


# Apply migrations
python manage.py makemigrations
python manage.py migrate

# Create a superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic --noinput

# Start the development server
python manage.py runserver


### If any permisssion issues use the command --> chmod with filename(setup.sh)
>>>>>>> cc8c42b1253e16d9e0c58fd52d5779c021689bba

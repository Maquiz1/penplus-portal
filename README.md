logbook
Setup
python3 -m pip install --user virtualenv
python3 -m venv venv
cd env
source bin/activate


## Install dependencies
pip install -r requirements.txt
pip freeze > requirements.txt
cat requirements.txt

## Run the app
Copy the .env.example file to .env and fill in the values
python app.py
Development
# Run the app
python manage.py makemigrations mentorship
python manage.py migrate

# Create a superuser
python manage.py createsuperuser --email admin@example.com --username admin 
python manage.py makemigrations mentorship
python manage.py runserver
Custom Template Filters
To use the custom template filters in your templates, add the following line at the top of each template:

{% load custom_filters %}



python manage.py collectstatic

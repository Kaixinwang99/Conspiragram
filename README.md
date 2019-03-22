# Conspiragram
The group work of WAD2

To run Conspiragram, you will need the django registration redux library, which can be installed using
pip install -U django-registration-redux==1.4

Additionally, the database must be set up with the specific command:
python manage.py migrate --run-syncdb
NOT just python manage.py migrate, that will cause errors in the population script.

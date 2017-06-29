# A walkthrough locallibrary website through MDN

## Getting Started

### Dependencies

- python 3.5.2
- virtualenv

After installing Python, use `pip` to install virtualenv.

  pip install virtualenv

Create a virtualenv environment for the project.

  virtualenv locallibrary_env

Activate the environment.

  source locallibrary_env/bin/Activate

Install the project requirements.

  pip install -r requirement.txt

### Run the application:
By default, the app is served at http://127.0.0.1:8000

  python manage.py runserver

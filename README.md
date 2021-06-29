# DRF API Template

### Installation
1. Create a virtual environment: `virtualenv -p python3.8.2 venv`
2. Activate the virtual environment: `source venv/bin/activate`
3. Install requirements: `pip install -r requirements.txt`
6. Create postgres database and user
4. Create .env file with environment variables, such as secret key and database
5. Load environment variables: `source .env`
7. Apply database migrations: `python manage.py migrate`
8. Create a local superuser: `python manage.py createsuperuser`

### Development
1. Activate the virtual environment: `source .env`
2. Start django server: `python manage.py runserver`

### Running script in python shell during development
1. Import script into run.py
2. Run the code in run.py in the python shell: `python manage.py shell < run.py`

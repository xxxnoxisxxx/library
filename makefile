VIRTUALENV_PATH = /usr/bin/python2.7
VIRTUALENV_NAME = ../env
PROJECT_NAME = library
DB_JSON = db.json

virtualenv:
	sudo pip2.7 install virtualenv
install:
	#@mkdir $(VIRTUALENV_NAME)
	virtualenv -p $(VIRTUALENV_PATH) $(VIRTUALENV_NAME)
	. $(VIRTUALENV_NAME)/bin/activate
	sudo pip2.7 install -r requirements.txt
	python manage.py makemigrations
	python manage.py migrate

migrate:
	. $(VIRTUALENV_NAME)/bin/activate
	python manage.py migrate

migrations:
	. $(VIRTUALENV_NAME)/bin/activate
	python manage.py makemigrations

run:
	. $(VIRTUALENV_NAME)/bin/activate
	python manage.py runserver 0.0.0.0:8000

#uwsgi:
#	sudo apt-get install python-dev

loaddata:
	. $(VIRTUALENV_NAME)/bin/activate
	python manage.py loaddata $(DB_JSON)

dump:
	. $(VIRTUALENV_NAME)/bin/activate
	python manage.py dumpdata --indent 2 > $(DB_JSON)

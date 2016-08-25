#!/bin/bash

VIRTUALENV_PATH="/usr/bin/python2.7"
VIRTUALENV_NAME="../env"
PROJECT_NAME="library"
DB_JSON="books/fixtures/initial_data.json"
PIP=$(ls /usr/bin/ | grep pip2)

prepare_env(){

	dpkg -l | grep pip >/dev/null
	if [ $? -ne 0 ]; then
		sudo apt-get install -y python-pip
	fi

	$PIP freeze | grep virtualenv >/dev/null
	if [ $? -ne 0 ]; then
		sudo $PIP install virtualenv
	fi
	
	if [ ! -d $VIRTUALENV_NAME ]; then
		virtualenv -p $VIRTUALENV_PATH $VIRTUALENV_NAME
	fi

	source $VIRTUALENV_NAME/bin/activate

	$PIP freeze | grep Django==1.9.8 >/dev/null
	if [ $? -ne 0 ]; then
		$PIP install Django==1.9.8
	fi

	$PIP freeze | grep crispy >/dev/null
	if [ $? -ne 0 ]; then
		$PIP install django-crispy-forms
	fi

	$PIP freeze | grep djangorestframework >/dev/null
	if [ $? -ne 0 ]; then
		$PIP install --upgrade djangorestframework
	fi

	$PIP freeze | grep bootstrap-admin >/dev/null
	if [ $? -ne 0 ]; then
		$PIP install bootstrap-admin
	fi

	$PIP install --upgrade selenium

	deactivate

	migrations
	migrate

}

migrate(){
	source $VIRTUALENV_NAME/bin/activate; 
	python manage.py migrate;
	deactivate
}

migrations(){
	source $VIRTUALENV_NAME/bin/activate; 
	python manage.py makemigrations;
	deactivate
}

run(){
	source $VIRTUALENV_NAME/bin/activate; 
	python manage.py runserver 0.0.0.0:8000;
	deactivate
}

loaddata(){
	migrations
	migrate
	source $VIRTUALENV_NAME/bin/activate; 
	echo "yes" | python manage.py flush
	python manage.py loaddata $DB_JSON;
	deactivate
}

dump(){
	source $VIRTUALENV_NAME/bin/activate; 
	python manage.py dumpdata --indent 2 > $DB_JSON;
	deactivate
}

collectstatic(){
	source $VIRTUALENV_NAME/bin/activate; 
	python manage.py collectstatic;
	deactivate
}

check_sw(){
	source $VIRTUALENV_NAME/bin/activate; 
	pip_sw=`pip freeze`
	echo $PIP_SW
	deactivate
}

check_sw(){
	source $VIRTUALENV_NAME/bin/activate; 
	pip_sw=`pip freeze`
	echo $PIP_SW
	deactivate
}

funtests(){
	source $VIRTUALENV_NAME/bin/activate; 
	python manage.py test functional_tests
	deactivate
}

mm(){
	migrations
	migrate
}




show_help(){
	echo "--------------------------------------------"
	echo "Usage: "
	echo "manager [OPTION]"
	echo ""
	echo "Possible options:"
	echo "    prepare"
	echo "    migrate"
	echo "    migrations"
	echo "    run"
	echo "    loaddata"
	echo "    dump"
	echo "    collectstatic"
	echo "    check_sw"
	echo "    funtests"
	echo "    mm"
}
#####################################################
#                       MAIN                        #
#####################################################
if [ "$#" -ne 1 ]; then
	echo "--------------------------------------------"
    echo "Error: Illegal number of parameters."
    show_help
    exit -1
fi

case "$1" in
  "prepare") 		prepare_env ;;
  "migrate") 		migrate ;;
  "migrations") 	migrations ;;
  "run") 			run ;;
  "loaddata") 		loaddata ;;
  "dump") 			dump ;;
  "collectstatic") 	collectstatic ;;
  "check_sw")       check_sw;;
  "funtests")       funtests;;
  "mm")       		mm;;
  *) 				show_help
esac

#http://stackoverflow.com/questions/1338728/delete-commits-from-a-branch-in-git
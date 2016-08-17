#!/bin/bash

VIRTUALENV_PATH="/usr/bin/python2.7"
VIRTUALENV_NAME="../env"
PROJECT_NAME="library"
DB_JSON="db.json"
PIP=$(ls /usr/bin/ | grep pip2)

prepare_env(){
	sudo apt-get install -y python-pip
	sudo $PIP install virtualenv

	virtualenv -p $VIRTUALENV_PATH $VIRTUALENV_NAME
	source $VIRTUALENV_NAME/bin/activate
	$PIP install Django==1.9.8
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
	source $VIRTUALENV_NAME/bin/activate; 
	python manage.py loaddata $(DB_JSON); 
	deactivate
}

dump(){
	source $VIRTUALENV_NAME/bin/activate; 
	python manage.py dumpdata --indent 2 > $(DB_JSON);
	deactivate
}

collectstatic(){
	source $VIRTUALENV_NAME/bin/activate; 
	python manage.py collectstatic; 
	deactivate
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
  *) 				show_help ;;
esac
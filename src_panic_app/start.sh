#!/bin/bash
source /root/.bashrc

#if gcloud auth list 2>/dev/null | grep -q active; then
#        echo Logged
#else
#        gcloud auth login
#fi

# two ways of autheticating with GCP

# BROWSER FLOW:
#gcloud auth login

# SERVICE ACCOUNT .p12 key : more on this at https://cloud.google.com/sdk/gcloud/reference/auth/activate-service-account
gcloud auth activate-service-account $SERVICE_ACCOUNT_EMAIL --key-file /credentials/key.p12 --password-file /credentials/password

gcloud config set project panic-tests

/usr/bin/python /panic_app/runapp.py
#uwsgi /panic_app/uwsgi.ini

<<COMMENT1

REPLY="y"
while [ "$REPLY" = "y" ]; do


	read -p "prod(uwsgi) or dev(flask)? (p/d) " REPLY2
	case "$REPLY2" in
		("p"|"P") uwsgi /panic_app/uwsgi.ini;;
		("d"|"D")    /usr/bin/python /panic_app/runapp.py;;
		(*) echo "Mal hecho,,, nos vamos!... bye! "; exit;;
	esac
	

	read -p "The server has stopped! Do I restart it? (y) " REPLY
	case "$REPLY" in
		(""|"E"|"e") exit;;
	esac
done
COMMENT1
#!/bin/bash
source /root/.bashrc

#if gcloud auth list 2>/dev/null | grep -q active; then
#        echo Logged
#else
#        gcloud auth login
#fi
gcloud auth login


REPLY="y"
while [ "$REPLY" = "y" ]; do


	read -p "prod or dev? (p/d) " REPLY2
	case "$REPLY2" in
		("p"|"P") uwsgi /root/panic_app/uwsgi.ini;;
		("d"|"D")    /usr/bin/python /root/panic_app/app/app.py;;
		(*) echo "Mal hecho,,, nos vamos!... bye! "; exit;;
	esac
	

	read -p "The server has stopped! Do I restart it? (y) " REPLY
	case "$REPLY" in
		(""|"E"|"e") exit;;
	esac
done

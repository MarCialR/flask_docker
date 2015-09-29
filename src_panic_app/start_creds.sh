#!/bin/bash
source /root/.bashrc

#if gcloud auth list 2>/dev/null | grep -q active; then
#        echo Logged
#else
#        gcloud auth login
#fi

#gcloud auth login
#ls panic_app
#https://cloud.google.com/sdk/gcloud/reference/auth/activate-service-account
gcloud auth activate-service-account <SERVICE_ACCOUNT_EMAIL> --key-file panic_app/key.p12 --password-file panic_app/password
gcloud config set project panic-tests

/usr/bin/python /root/panic_app/runapp.py

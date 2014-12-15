panic
=====

sudo docker build -t marcialr/panic:3_pexpect .
sudo docker build -t marcialr/panic:4_tornado .


sudo docker run -i -t -p 8080:8080  --name panic -v /home/marcial/repos/flask_docker/src_panic_app:/root/panic_app/ marcialr/panic:3_pexpect /root/panic_app/app/start.sh


sudo docker run -i -t -p 10.240.166.172:8899:8080 --name panic -v /home/mroman/repos/flask_docker/panic/src_panic_app:/root/panic_app/ marcialr/panic:3_pexpect /root/panic_app/start.sh

sudo docker run -i -t -p 10.240.166.172:8899:8080 --name panic -v /home/mroman/repos/flask_docker/panic/src_panic_app:/root/panic_app/ marcialr/panic:4_uwsgi /root/panic_app/start.sh


Inspect container
-----------------
sudo docker inspect panic_containery


dependencies
============
flask
flask-restful
pexpect

add cloud sdk
https://cloud.google.com/sdk/https://www.youtube.com/watch?v=Rs38x-13l9s
https://registry.hub.docker.com/u/google/cloud-sdk/

theme
=====
git clone https://github.com/IronSummitMedia/startbootstrap-sb-admin.git startbootstrap-sb-admin

docs
====

flask
http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ii-templates

flask-restful
https://flask-restful.readthedocs.org/en/0.3.0/quickstart.html#a-minimal-api

configuration
http://maximebf.com/blog/2012/10/building-websites-in-python-with-flask/#.VIVjxerd-kA

postgres
========
imagen => https://registry.hub.docker.com/_/postgres/


investigar
==========
http://haifux.org/lectures/294/modern-web-applications.pdf
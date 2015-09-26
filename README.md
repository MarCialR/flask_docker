panic
=====

docker build -t marcialr/panic:4_panic .

docker run -it -p 8080:8080  --name panic -v $(pwd)/src_panic_app:/root/panic_app/ panic /root/panic_app/start.sh

If from an instance: -p <EXTERNAL_IP>:8899:8080 


Inspect container
-----------------
sudo docker inspect panic


dependencies
============
flask
flask-restful
pexpect
uwsgi
nose



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

to think
======== 
http://code.activestate.com/recipes/159571-importing-any-file-without-modifying-syspath/

GitHub
======
https://github.com/MarCialR/flask_docker.git



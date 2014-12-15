############################################################
# Dockerfile to build Python WSGI Application Containers
# Based on Ubuntu
# Hints at:
#	https://www.digitalocean.com/community/tutorials/docker-explained-how-to-containerize-python-web-applications
#	https://github.com/MarCialR/flask_docker/blob/master/Dockerfile
############################################################


FROM marcialr/panic:4_uwsgi

# Copy the application folder inside the container
ADD /src_panic_app /root/panic_app

# Get pip to download and install requirements:
RUN pip install -r /root/panic_app/requirements.txt

WORKDIR /root/panic_app

EXPOSE 8080


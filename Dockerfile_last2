############################################################
# Dockerfile to build Python WSGI Application Containers
# Based on Ubuntu
# Hints at:
#	https://www.digitalocean.com/community/tutorials/docker-explained-how-to-containerize-python-web-applications
#	https://github.com/MarCialR/flask_docker/blob/master/Dockerfile
############################################################


FROM marcialr/panic:2_gcloud_sdk

# File Author / Maintainer
MAINTAINER MarCialR <marcialemilio@gmail.com>


# Copy the application folder inside the container
ADD /src_panic_app /root/panic_app

RUN apt-get install -y python-dev

# Get pip to download and install requirements:
RUN pip install -r /root/panic_app/requirements.txt

# Install Nginx.
#RUN apt-get install -y nginx && \
#  rm -rf /var/lib/apt/lists/* && \
#  echo "\ndaemon off;" >> /etc/nginx/nginx.conf && \
#  chown -R www-data:www-data /var/lib/nginx

# Define mountable directories.
#VOLUME ["/etc/nginx/sites-enabled", "/etc/nginx/certs", "/etc/nginx/conf.d", "/var/log/nginx"]

# Define working directory.
#WORKDIR /etc/nginx

WORKDIR /root/panic_app
#RUN git clone https://github.com/IronSummitMedia/startbootstrap-sb-admin.git startbootstrap-sb-admin

EXPOSE 8080

# ENTRYPOINT ["/bin/bash", "/root/panic_app/start.sh"]


############################################################
# Dockerfile to build Python WSGI Application Containers
# Based on Ubuntu
# More Hints at:
#	https://www.digitalocean.com/community/tutorials/docker-explained-how-to-containerize-python-web-applications
#	https://github.com/GoogleCloudPlatform/cloud-sdk-docker/blob/master/Dockerfile
#	https://github.com/MarCialR/flask_docker/blob/master/Dockerfile
############################################################


# Set the base image to Ubuntu
FROM google/debian:wheezy

# File Author / Maintainer
MAINTAINER MarCialR <marcialemilio@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

# Install Python and Basic Python Tools
# -------------------------------------
RUN apt-get update && apt-get install -y -qq --no-install-recommends wget \
	unzip \
	python \
	python-pip \
	python-dev \
	build-essential \
	php5-mysql \
	php5-cli \
	php5-cgi \
	openjdk-7-jre-headless \
	openssh-client \
	python-openssl \
	build-essential \
	&& apt-get clean


# Install Gcloud SDK
# ------------------
RUN wget https://dl.google.com/dl/cloudsdk/release/google-cloud-sdk.zip && \
	unzip google-cloud-sdk.zip && \
	rm google-cloud-sdk.zip

ENV CLOUDSDK_PYTHON_SITEPACKAGES 1

RUN google-cloud-sdk/install.sh --usage-reporting=true --path-update=true --bash-completion=true --rc-path=/.bashrc --disable-installation-options

# Udpate Cloud SDK components
# ---------------------------
RUN google-cloud-sdk/bin/gcloud --quiet components update preview alpha beta app app-engine-java app-engine-python

RUN google-cloud-sdk/bin/gcloud --quiet config set component_manager/disable_update_check true

# Install AppEngine Python SDK
# ----------------------------
#VAR appengine_SDK_URL=https://storage.googleapis.com/appengine-sdks/featured/google_appengine_1.9.26.zip
RUN wget https://storage.googleapis.com/appengine-sdks/featured/google_appengine_1.9.26.zip
RUN unzip google_appengine_1.9.26.zip
RUN rm google_appengine_1.9.26.zip


# Install My Application
# ----------------------
# Copy the application folder inside the container
ADD /src_panic_app/requirements.txt /root/panic_app/requirements.txt
# Get pip to download and install requirements:
RUN pip install -r /root/panic_app/requirements.txt



WORKDIR /root/panic_app

EXPOSE 8080

RUN mkdir /.ssh
ENV PATH /google_appengine:/google-cloud-sdk/bin:$PATH
ENV HOME /
VOLUME ["/.config"]
#CMD ["/bin/bash"]
CMD ["/root/panic_app/start.sh"]

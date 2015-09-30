####################################################################
# Dockerfile to build a WSGI Flask app that runs Gcloud Commands
#
# Based on Ubuntu
#
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
ENV PATH /google-cloud-sdk/bin:$PATH

# Install AppEngine Python SDK
# ----------------------------
#VAR appengine_SDK_URL=https://storage.googleapis.com/appengine-sdks/featured/google_appengine_1.9.26.zip
RUN wget https://storage.googleapis.com/appengine-sdks/featured/google_appengine_1.9.26.zip
RUN unzip google_appengine_1.9.26.zip
RUN rm google_appengine_1.9.26.zip
ENV PATH /google_appengine:$PATH


# Install Application requirements
# --------------------------------
# Copy the application folder inside the container
COPY /src_panic_app/requirements.txt /requirements.txt
# Get pip to download and install requirements:
RUN pip install -r /requirements.txt
RUN rm requirements.txt



# Install My Application
# ----------------------

WORKDIR /
COPY /src_panic_app/ panic_app
COPY /credentials/ credentials

EXPOSE 8080
CMD ["/panic_app/start.sh"]


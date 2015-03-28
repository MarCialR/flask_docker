# /usr/bin/bash

#DOCKER
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 36A1D7869245C8950F966E92D8576A8BA88D21E9
sudo sh -c "echo deb https://get.docker.com/ubuntu docker main\
> /etc/apt/sources.list.d/docker.list"

# GOOGLE CHROME
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
sudo sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'

sudo apt-get update

sudo apt-get install -y google-chrome-stable
#sudo apt-get install google-chrome-beta
#sudo apt-get install google-chrome-unstable

sudo apt-get install -y lxc-docker

sudo apt-get install -y zsh
wget -O ~/.zshrc http://git.grml.org/f/grml-etc-core/etc/zsh/zshrc

sudo apt-get install -y nano
sudo apt-get install -y gparted
sudo apt-get install -y nmon
sudo apt-get install -y tree
sudo apt-get install -y tmux
sudo apt-get install -y shutter
sudo apt-get install -y parcellite
#sudo apt-get install lxappearance

sudo apt-get install -y python-pip

mkdir ~/.virtualenvs
sudo pip install virtualenv
sudo pip install virtualenvwrapper


#sudo apt-get install krita
#sudo apt-get install xdotool

#Set WORKON_HOME to your virtualenv dir
#export WORKON_HOME=~/.virtualenvs
#Add virtualenvwrapper.sh to .bashrc

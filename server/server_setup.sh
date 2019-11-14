#!/usr/bin/env bash

# Consider running these two commands separately
# Do a reboot before continuing.
apt update
apt upgrade -y

apt install zsh
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

# Install some OS dependencies:
sudo apt-get install -y -q build-essential git unzip zip nload tree
sudo apt-get install -y -q python3-pip python3-dev python3-venv
sudo apt-get install -y -q nginx
# for gzip support in uwsgi
sudo apt-get install --no-install-recommends -y -q libpcre3-dev libz-dev

# Stop the hackers
sudo apt install fail2ban -y

ufw allow 22
ufw allow 80
ufw allow 443
ufw enable

# Basic git setup
git config --global credential.helper cache
git config --global credential.helper 'cache --timeout=720000'

# Be sure to put your info here:
git config --global user.email "inderpreet_dhillon@hotmail.com"
git config --global user.name "Inderpreet Dhillon"

# Web app file structure
mkdir /apps
chmod 777 /apps
mkdir /apps/logs
mkdir /apps/logs/treachery
mkdir /apps/logs/treachery/app_log
cd /apps

# Create a virtual env for the app.
cd /apps
python3 -m venv venv
source /apps/venv/bin/activate
pip install --upgrade pip setuptools
pip install --upgrade httpie glances
pip install --upgrade uwsgi


# clone the repo:
cd /apps
git clone https://github.com/DragynSlayr/TreacheryApp.git app_repo

# Setup the web app:
cd /apps/app_repo/Treachery/
pip install -r requirements.txt

# Copy and enable the daemon
cp /apps/app_repo/server/treachery.service /etc/systemd/system/treachery.service

systemctl start treachery
systemctl status treachery
systemctl enable treachery

# Setup the public facing server (NGINX)
apt install nginx

# CAREFUL HERE. If you are using default, maybe skip this
rm /etc/nginx/sites-enabled/default

cp /apps/app_repo/server/treachery.nginx /etc/nginx/sites-enabled/treachery.nginx
update-rc.d nginx enable
service nginx restart


# Optionally add SSL support via Let's Encrypt:
# https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-18-04

add-apt-repository ppa:certbot/certbot
apt install python-certbot-nginx
certbot --nginx -d treachery-mtg.ca

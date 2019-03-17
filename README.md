# Django-basic-pratice
實作一個模擬房地產網站來練習django framework
# About
為了練習django framework基本功能，建立一個模擬房地產網站
後端由django framework寫成，前端則用bootstrap4及jquery
webserve部署於Digital ocean上
### Domain
未部署
# Develop Environment
Windows 10 Home
# Usage
## Local
複製專案
```
git clone https://github.com/Mchighlight/django-basic-pratice.git
```
建立virtual environment
```
py -m virtualenv venv
```
啟動virtual environment
```
.\venv\Scripts\activate
```
安裝packages
```
pip install -r requirements.txt
```
Migrations
```
python manage.py makemigrations && python manage.py migrate
```
Load database data 
```
python manage.py loaddata \realtor\fixture.json && 
python manage.py loaddata \listing\fixture.json 
```
local起server
```
python manage.py runserver 8000
```
The server will then be available at http://127.0.0.1:8000
## Docker
未實作
# TODO
* add docker container

#How to deploy on Digital Ocean
All of the command run on the git bash, $ sign means running on your local machine. On the other hand,  # signs means running on the server
## Creating SSH Keys
Generate a key on your local machine, I'm using git bash
```
$ ssh-keygen
```
You will create a public and private key at, you should keep the private key in your local machine, and it should not known by others 
```
id_rsa
id_rsa.pub
```
Copy the public key
```
$ cat id_rsa.pub
```
Copy the entire output  and add as an SSH key for Digital Ocean


# Login to Your Server
if you setup SSH keys correctly the command below will let you right in, If you did not use SSH keys, it will ask for a password. This is one that was mailed to you
```
$ ssh root@YOUR_SERVER_IP
```
if you get denied run these two command below
```
$ eval `ssh-agent -s`
$ ssh-add id_rsa
```

# Create a new user
It will ask for password . add the user name you want it, and some other personal info
```
# adduser henry_huang
```

# Give root privileges
```
# usermod -aG sudo djangoadmin
```

# SSH keys for the new user
Now we need to setup SSH keys for the new user. You will need to get them from your local machine
## Exit the sserver
You need to copy the key from your local machine so either exit or open a new terminal
```
# exit
```
You can generate a different key if you want but we will use the same one so les output it, select it then copen it
```
$ cat id_rsa.pub
```
## Log back into the server
```
$ ssh root@YOUR_SERVER_IP
```

## Add SSH key for new user
Navigate to the new users home folder and create a file at '.ssh/authorized_keys' and paste in the key
```
# cd /home/henry_huang
# mkdir .ssh
# cd .ssh
# nano authorized_keys
Paste the key and save it
```
ps: the public ssh key must be same

## Loging as new user
Now you should log in  as new user successfully
$ ssh henry_huang@YOUR_SERVER_IP

# Disable root login
```
sudo nano /etc/ssh/sshd_config
```

# Change the following
```
PermitRottLogin no
PasswordAuthentication no
```

# Reload sshd service
```
sudo systemctl realod sshd
```






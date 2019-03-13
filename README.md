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
python manage.py loaddata \listing\fixture.json &&
python manage.py loaddata \contact\fixture.json &&
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

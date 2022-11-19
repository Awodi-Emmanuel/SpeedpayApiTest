# SpeedpayApiTest
A FintechAPIs test with 

Logic Implementation
1. User authentication  (registeration and login)
2. create a new user via Api
3. make deposit via api
4. make a withdrawal via api
5. Check Balance

Step by step guid to building the api

Step 1

Create a GitHub [Projectname] and clone on host 

To clone the github repo navigate to a directory on your pc 
```
git clone [Projectname]

```
navigate to the project directory like so. 

```
cd Python-Django-Bank-Application
```
open with vscode
I created my virtual environment and activated with 

Step 2

Create a postgresql database
	1. database name: speedpayapi
	2. database user: speedpay
	3. database pass: Speed123_

Step 3
```
  pip install django 
  
```
pip is used to install python packages

Step 4

django-admin startapp [myproject name]
```
django-admin startproject [djangoproject .]
```

python manage.py startapp [myapp name]
```
python manage.py startapp [appname]
```
include myapp name in install apps in settings


Step 5 

connect my database to postgresql
install a package call psycopg2 to be able 
to connect to postgres databse
```
pip install psycopg2

```
Step 6

> create model
> User models

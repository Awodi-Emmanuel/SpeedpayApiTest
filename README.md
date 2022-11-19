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

Create a GitHub [Projectname] and clone it to your host os

To clone the github repo navigate to a directory on your pc 
```
git clone [Projectname]

```
Step 2

navigate to the project directory like so. 

```
cd Python-Django-Bank-Application
```
Step 3

open project with vscode by typing
```
code .
```
Step 4

create a virtual environment if you already have it setup with python  on 
your computer.

``` 
virtualenv env
```

Step 5

Create a postgresql database on your terminal different from your vscode
	

Step 6

Inside your project open in vscode run ro install django after activating your virtualenv 
```
  pip install django 
  
```
pip is used to install python packages

Step 7


start a new django project by running this django-admin startapp [myproject name]
```
django-admin startproject [djangoproject .]
```
Step 8


To start your project run python manage.py startapp [myapp name]
```
python manage.py startapp [appname]
```
include your appname in install apps in settings


Step 9

run pip requirements.txt to be able to  work with 
the project. 

```
pip freeze > requirements.txt 

```

Step 10

Make your migrations by running 

```
python manage.py makemigrations
```
And also
```
python manage.py migrate 
```
Your App is ready for use!

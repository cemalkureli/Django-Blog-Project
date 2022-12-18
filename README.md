# Django-Blog-Project


### Development 👨‍💻
**Note** : Make sure you have Python version 3.8+


### Environment Setup 🚀

`$ git clone https://github.com/cemalkureli/Django-Blog-Project.git`

`$ cd django_project_blogapp/`


If virtualenv is not installed;

`$ pip install virtualenv`


Create a virtual environment

`$ virtualenv venv`


Activate the environment everytime you open the project

`$ source venv/Scripts/activate`


Install requirements 🛠

`$ pip install -r requirements.txt`


Run migrations for Database 

`$ python manage.py makemigrations`

`$ python manage.py migrate`


Create superuser for Admin Login 🔐

`$ python manage.py createsuperuser`


All Set! 🤩


Now you can run the server to see your application up & running 🚀

`$ python manage.py runserver`


To exit the environment ❎

`$ deactivate`


Every time you want to open the application in browser, make sure you run:

`$ source venv/Scripts/activate`

`$ python manage.py runserver`

# Django-Blog-Project


### Development 👨
**Note** : Make sure you have Python version 3.10+


### Environment Setup 

`$ mkdir folder_name`

`$ cd folder_name`

`$ git clone https://github.com/cemalkureli/Django-Blog-Project.git`

`$ cd Django-Blog-Project/`


If virtualenv is not installed;

`$ pip install virtualenv`


Create a virtual environment

`$ virtualenv venv`


Activate the environment everytime you open the project

`$ source venv/Scripts/activate`


Install requirements 🛠

`$ pip install -r requirements.txt`


Run migrations for Database 

`$ cd django_web` (make sure the manage.py file is in the correct folder)

`$ python manage.py makemigrations`

`$ python manage.py migrate`


Create superuser for Admin Login 🔐

`$ python manage.py createsuperuser`


Python asks if you create superuser;

`Username: `
`Email: `
`Password: `
`Password Again: `


All Set! 🤩


Now you can run the server to see your application up & running 🚀

`$ python manage.py runserver`


To exit the environment ❎

`CTRL + C --> to exit runserver`

`$ deactivate --> to exit venv`


Every time you want to open the application in browser, make sure you run:

`$ source venv/Scripts/activate`

`$ python manage.py runserver`



If you get AttributeError: module 'collections' has no attribute 'Iterator' error;

You should check your pip modules;

`$ pip list `

If the modules in the requirements.txt are outdated, replace them with your own modules, save the requirements.txt again 
and redo the installation steps from the beginning. 🤩🤩🤩


After all these steps , you can start testing and developing this project.

### That's it! 👨



# Heroku Django Quickstart


## Create a Heroku app

### Check that you have python installed

`$ python3 -V` -> `Python 3.7.3`

### Check that you have Django installed

`$ python3 -m django --version` -> `2.2.13`

If Django is installed, you should see the version of your installation. If it isn’t, you’ll get an error telling “No module named django”.

### Create a project

`$ django-admin startproject [projectname]`

> *Note: You’ll need to avoid naming projects after built-in Python or Django components. In particular, this means you should avoid using names like  `django`  (which will conflict with Django itself) or  `test`  (which conflicts with a built-in Python package).*

### Run locally

`$ python manage.py runserver`

*[troubleshooting for this section](https://docs.djangoproject.com/en/3.0/intro/tutorial01/)*




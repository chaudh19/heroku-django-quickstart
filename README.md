# Heroku Django Quickstart


## Create a Heroku app

### Python setup

`$ python3 -V` -> `Python 3.7.3`

### Django setup

`$ python3 -m django --version` -> `2.2.13`

If Django is installed, you should see the version of your installation. If it isn’t, you’ll get an error telling “No module named django”.

### Create a Django project

`$ django-admin startproject [projectname]`

> *Note: You’ll need to avoid naming projects after built-in Python or Django components. In particular, this means you should avoid using names like  `django`  (which will conflict with Django itself) or  `test`  (which conflicts with a built-in Python package).*

### Run locally

`$ python manage.py runserver`

*[troubleshooting for this section](https://docs.djangoproject.com/en/3.0/intro/tutorial01/)*

## Get Ready to Deploy


### Heroku setup

To verify your CLI installation, use the  `heroku --version`  command:
```
$ heroku --version` -> `$ heroku/7.0.0 (darwin-x64) node-v8.0.0
```

After you install the CLI, run the `heroku login` command.

Now you’re ready to create your first Heroku app:
```
heroku create
```

*[troubleshooting for this section](https://devcenter.heroku.com/articles/heroku-cli)*

### Github setup
`git --version` -> `git version 2.21.0 (Apple Git-122.2)`

*[troubleshooting for this section](https://confluence.atlassian.com/crucible042/installing-and-upgrading-git-869175555.html)*

### Getting Ready to Deploy

Before we can push our Django app to Heroku, Heroku needs a little more information on how to run the app.

Specifically, Heroku needs 6 changes to our out-of-the-box Django app:

1.  Gunicorn
2.  Procfile
3.  django-heroku
4.  STATIC_ROOT  /  PROJECT_ROOT in settings.py
5.  requirements.txt
6.  runtime.txt


#### 1. Gunicorn

Gunicorn is an open-source web server for Python. It allows Heroku to deploy our application across various “workers.” In your project’s directory, run:

```
$ python3
>>> import gunicorn
>>> print(gunicorn.__version__)
20.0.4
```

if you don't see it run:
```
pip3 install gunicorn
```

#### 2. dj-database-url + psycopg2-binary

 In your project’s directory, run:

```
$ pip3 install dj-database-url
$ pip3 install psycopg2
```

If `pip3 install psycopg2` isn't working, try `pip3 install psycopg2==2.7.5`

Then add the following to the bottom of  `settings.py`:

```
import dj_database_url
DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)
```

This will parse the values of the  `DATABASE_URL`  environment variable and convert them to something Django can understand.

#### 3. Procfile

A Procfile is something unique to Heroku. It’s a file in your project’s root directory that tells Heroku how your app should start and run.

In our case, we’ll use our Procfile to tell Heroku to run a Gunicorn server.

The good news is Django comes with out-of-the-box support for Gunicorn servers, because they both follow the conventions of [WSGI](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface).

In the Procfile, we’ll tell Heroku to start a Gunicorn server and then point that server to our Django project’s default WSGI interface.

In  `[projectname]/`  , run the following command to create the Procfile:

```
echo 'web: gunicorn [projectname].wsgi --log-file -' > Procfile
```

You’ll need to replace  `[projectname].wsgi`  with  `your_project_name.wsgi`.

#### 3. django-heroku

Django is a pretty popular framework, so Heroku has created a module called [django-heroku](https://github.com/heroku/django-heroku)  that helps with settings, testing, and logging automatically.

To install it, make sure you’re in  `[projectname]/`  then:

`pip3 install django-heroku`

With the module successfully installed, we can now add it to our Django project’s  `settings.py`.

Open  `[projectname]/[projectname]/settings.py`.
At the top of  `settings.py`  import the module. Then, at the very bottom, call it:

```
import django_heroku
...# All of your settings here...
django_heroku.settings(locals())
```

*[troubleshoot this section](https://devcenter.heroku.com/articles/django-app-configuration)*

Save  `settings.py`, but don’t close it. We have more changes to make.

#### 4. STATIC_ROOT & PROJECT_ROOT

Search your  `settings.py`  for an environment variable called  `STATIC_URL`.

Next to that setting, we’ll also need to give Heroku more context about where static files (images, scripts, etc) are stored.

We’ll add two new variables, `STATIC_ROOT` and `PROJECT_ROOT`, in addition to `STATIC_URL`. That section of `settings.py` should now look like this:

```
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))  
STATIC_URL = '/static/'  
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
```

#### 5. whitenoise

Edit your settings.py file and add WhiteNoise to the MIDDLEWARE list. The WhiteNoise middleware should be placed directly after the Django SecurityMiddleware (if you are using it) and before all other middleware:

```
MIDDLEWARE = [
  'django.middleware.security.SecurityMiddleware',
  'whitenoise.middleware.WhiteNoiseMiddleware',
  # ...
]
```

That’s it – WhiteNoise will now serve your static files (you can confirm it’s working using the steps below). 

*(the below whitenoise configs are optional)*

WhiteNoise comes with a storage backend which automatically takes care of compressing your files and creating unique names for each version so they can safely be cached forever. To use it, just add this to your  `settings.py`:

`STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'`

*[troubleshoot this section](http://whitenoise.evans.io/en/stable/django.html#django-middleware)*

#### 6. requirements.txt

Next, we need to tell Heroku about all the packages we’ve installed:

- dj-database-url
- Django
- django-heroku
- gunicorn
- psycopg2
- psycopg2-binary
- pytz
- whitenoise

Make sure you’re in the  `[project_name]`  directory, then:

`pip3 freeze > requirements.txt`

Check out  `requirements.txt`  to make sure it looks right:

```
dj-database-url==0.5.0
Django==2.2.13
django-heroku==0.3.1
gunicorn==20.0.4
psycopg2==2.7.5
pytz==2019.3
whitenoise==4.1.4
```

As you build your Django project, chances are you’ll find some other module you need. If so, don’t forget to  `pip3 freeze > requirements.txt`  whenever you deploy those changes.

## 6. runtime.txt

The final thing we need to do before deploying is tell Heroku what version of Python to use.

`echo 'python-3.7.3' > runtime.txt`

## Deploy
### 1. Add your project’s files to Git
```
git init
git add .
```
### 2. Commit the files to Git
```
git commit -am "init"
```

### 3. Push the files to the Heroku repository

```
git push heroku master
```

## Push to github
### 1. Create a new repository
You can visit [this page](https://github.com/new). Don't initialize it with a README

### 2. Create a README
```
echo "# test" >> README.md
```

### 3. Push the existing repository from the command line
```
git remote add origin https://github.com/chaudh19/test.git
git push -u origin master
```


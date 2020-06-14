# Heroku Django Quickstart


## Create a Heroku app

### Check your Python setup

```
$ python3 -V
>> Python 3.7.3
```

### Check your Django setup

```
$ python3 -m django --version
>> 2.2.13
```

If Django is installed, you should see the version of your installation. If it isn’t, you’ll get an error telling “No module named django”.

### Create a Django project

`$ django-admin startproject [projectname]`

> *Note: You’ll need to avoid naming projects after built-in Python or Django components. In particular, this means you should avoid using names like  `django`  (which will conflict with Django itself) or  `test`  (which conflicts with a built-in Python package).*

### Run locally

```
$ cd [projectname]
$ python3 manage.py runserver
```

Open `localhost:8000` and see the app in action!

*[troubleshooting for this section](https://docs.djangoproject.com/en/3.0/intro/tutorial01/)*

## Get ready to deploy


### Heroku setup

Verify your Heroku CLI installation with the  `heroku --version`  command:
```
$ heroku --version
>> heroku/7.0.0 (darwin-x64) node-v8.0.0
```

Next, run the `heroku login` command.

Now you’re ready to create your first Heroku app:
```
heroku create
```

*[troubleshooting for this section](https://devcenter.heroku.com/articles/heroku-cli)*

### Git setup
Verify your git setup with the  `git --version`  command:
```
$ git --version
>> git version 2.21.0 (Apple Git-122.2)
```

*[troubleshooting for this section](https://confluence.atlassian.com/crucible042/installing-and-upgrading-git-869175555.html)*

### Get ready to deploy

Before we can push our Django app to Heroku, Heroku needs a little more information on how to run the app.

Specifically, Heroku needs 6 changes to our out-of-the-box Django app:

1.  Gunicorn
2.  Procfile
3.  django-heroku
4.  STATIC_ROOT  /  PROJECT_ROOT in settings.py
5.  requirements.txt
6.  runtime.txt


#### 1. Gunicorn

Gunicorn is an open-source web server for Python. It allows Heroku to deploy our application across various “workers.” In your project’s directory, verify that you have gunicorn:

```
$ python3
>>> import gunicorn
>>> print(gunicorn.__version__)
20.0.4
>>> quit()
```

If you don't see it run:
```
pip3 install gunicorn
```

#### 2. psycopg2-binary

In your project’s directory, verify that you have psycopg2:
```
$ python3
>>> import psycopg2
>>> print(psycopg2.__version__)
2.7.5 (dt dec pq3 ext lo64)
>>> quit()
```
If you don't see it run:
```
$ pip3 install psycopg2
```

If `pip3 install psycopg2` isn't working, try `pip3 install psycopg2==2.7.5`


#### 3. Procfile

A Procfile is something unique to Heroku. It’s a file in your project’s root directory that tells Heroku how your app should start and run.

In our case, we’ll use our Procfile to tell Heroku to run a Gunicorn server.

The good news is Django comes with out-of-the-box support for Gunicorn servers, because they both follow the conventions of [WSGI](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface).

In the Procfile, we’ll tell Heroku to start a Gunicorn server and then point that server to our Django project’s default WSGI interface.

In `[projectname]/`, run the following command to create the Procfile:

```
echo 'web: gunicorn [projectname].wsgi' > Procfile
```

You’ll need to replace [projectname] with your project name

#### 3. django-heroku

Django is a pretty popular framework, so Heroku has created a module called [django-heroku](https://github.com/heroku/django-heroku) that helps with settings, testing, and logging automatically.

To install it, make sure you’re in the same folder as `manage.py` then:

```
$ python3
>>> import django_heroku
>>> quit()
```

If you see an error like `ModuleNotFoundError: No module named 'django_heroku'`, then run:
```
$ pip3 install django-heroku
```

With the module successfully installed, we can now add it to our Django project’s `settings.py`.

Open `settings.py`. 
At the top of `settings.py`, import the module. Then, at the very bottom, call it:

```
import django_heroku
...# All of your settings here...
django_heroku.settings(locals())
```

*[troubleshoot this section](https://devcenter.heroku.com/articles/django-app-configuration)*

Save  `settings.py`, but don’t close it. We have more changes to make.

#### 4. STATIC_ROOT & PROJECT_ROOT

Search your `settings.py` for an environment variable called `STATIC_URL`.

Next to that setting, we’ll also need to give Heroku more context about where static files (images, scripts, etc) are stored.

We’ll add two new variables, `STATIC_ROOT` and `PROJECT_ROOT`, in addition to `STATIC_URL`. That section of `settings.py` should now look like this:

```
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))  
STATIC_URL = '/static/'  
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
```

#### 5. whitenoise

WhiteNoise helps Django manage static files (images, scripts, etc) to load your site faster. Edit your `settings.py` file and add WhiteNoise to the MIDDLEWARE list. The WhiteNoise middleware should be placed directly after the Django SecurityMiddleware (if you are using it) and before all other middleware:

```
MIDDLEWARE = [
  'django.middleware.security.SecurityMiddleware',
  'whitenoise.middleware.WhiteNoiseMiddleware',
  # ...
]
```

That’s it – WhiteNoise will now serve your static files (you can confirm it’s working using the steps below). 

Django has a variable that lets it know where to store and retrieve static files. Let’s point it to WhiteNoise.

```
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

Add it above in the same place as your `STATIC_URL` and `STATIC_ROOT` variables.

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

Make sure you’re in the `[project_name]` directory, then:

`pip3 freeze > requirements.txt`

Check out  `requirements.txt`  to make sure it looks right:

```
dj-database-url==0.5.0 (we'll add this later)
Django==2.2.13
django-heroku==0.3.1
gunicorn==20.0.4
psycopg2==2.7.5
psycopg2-binary==2.8.5
python-dotenv==0.13.0 (we'll add this later)
pytz==2019.3
whitenoise==4.1.4
```

As you build your Django project, chances are you’ll find some other module you need. If so, don’t forget to  `pip3 freeze > requirements.txt` whenever you deploy those changes.

## 6. runtime.txt

The final thing we need to do before deploying is tell Heroku what version of Python to use.

```
$ echo 'python-3.7.3' > runtime.txt
```

## Deploy
### 1. Add your project’s files to Git
Do this in the same folder as `manage.py`:
```
$ git init
$ git add .
$ touch .gitignore
```

### 2. Create a .gitignore file

Now `open .gitignore` with your favorite text editor and paste in the following information about files Git should ignore:

```
### Django ###
*.log
*.pot
*.pyc
__pycache__/
local_settings.py
```
Now, you won’t bog down the deployment process with your log and cache files. We’ll keep Heroku nice and clean. Below, we’ll add `db.sqlite` to this list because we’ll be using a different database on Heroku.

### 3. Commit the files to Git
```
$ git commit -am "init"
```

### 4. Push the files to the Heroku repository

```
$ git push heroku master
```

## Push to github
### 1. Create a new repository
You can visit [this page](https://github.com/new). Don't initialize it with a README

### 2. Create a README
```
$ echo "# test" >> README.md
```

### 3. Push the existing repository from the command line
```
$ git remote add origin https://github.com/chaudh19/[NAME OF REPO].git
$ git push -u origin master
```

## Using Postgres Remotely & SQLite Locally

The key thing we’ll be doing here is setting `DATABASE_URL` to the Heroku-provided variable when we’re on Heroku. When we’re working locally, we’ll use a local file — `.env` — to set `DATABASE_URL` to point to SQLite. That way, any time we use the `DATABASE_URL` variable it will point to the correct database based on the environment.

```
pip3 install python-dotenv
```
This installs `python-dotenv` and also a related module called `dj-database-url`.

Add the new modules to your `requirements.txt`:
```
pip3 freeze > requirements.txt
```

### Create .env
We’ll use a file called `.env` to tell Django to use SQLite when running locally. To create `.env` and have it point Django to your SQLite database:
```
echo 'DATABASE_URL=sqlite:///db.sqlite3' > .env
```
Now, we don’t want .env to make it to Heroku, because .env is the part of our app that points to SQLite and Heroku doesn’t like SQLite.
So, we need git to ignore .env when pushing to Heroku. Run:
Add `.env` to `.gitignore`

### Update settings.py
Now that we have a `.env` file, we need to tell Django to use it. Hence why we downloaded the `python-dotenv` plugin earlier.

In your project’s `settings.py` make the following changes to get Django to use `.env`.
#### 1. Import new modules at the top of the file:
```
import dj_database_url
import dotenv
```
#### 2. Load environment variables from .env if it exists:
```
# This line should already exist in your settings.py
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# This is new:
dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)
```
Since `.env` won’t exist on Heroku, `dotenv.load_dotenv(dotenv_file)` will never get called on Heroku and Heroku will proceed to try to find its own database — Postgres.

#### 3. Change `DATABASES`

Currently your `settings.py` has this:
```
DATABASES = {    
    'default': {        
        'ENGINE': 'django.db.backends.sqlite3',        
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),    
    }
}
```
Change it to this:
```
DATABASES = {}
DATABASES['default'] = dj_database_url.config(conn_max_age=600)
```

The idea here is to clear the `DATABASES` variable and then set the `'default'` key using the `dj_database_url` module. This module uses Heroku’s `DATABASE_URL` variable if it’s on Heroku, or it uses the `DATABASE_URL` we set in the `.env` file if we’re working locally.

#### 4. sslmode issue workaround

If you ran the Django application as specified above, you might get an error when working locally because the `dj_database_url` module wants to log in with SSL. Heroku Postgres requires SSL, but SQLite doesn’t need or expect it.
So, we’ll use a hacky workaround to get dj_database_url to forget about SSL at the last second.
As the very last line in your `settings.py`, add:
```
# This should already be in your settings.py
django_heroku.settings(locals())
# This is new
del DATABASES['default']['OPTIONS']['sslmode']
```
#### 5. Try it out!

Locally:
```
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ python3 manage.py createsuperuser
$ python3 manage.py runserver
```

And on heroku
```
$ git commit -am "new db changes"
$ git push heroku master
$ heroku run python3 manage.py migrate
$ heroku run python3 manage.py createsuperuser
$ heroku open
```

# debugging

```
$ heroku logs --tail
```

sources:
- https://medium.com/@BennettGarner/deploying-django-to-heroku-procfile-static-root-other-pitfalls-e7ab8b2ba33b
- https://blog.usejournal.com/deploying-django-to-heroku-connecting-heroku-postgres-fcc960d290d1
- https://github.com/bennett39/django-heroku-example
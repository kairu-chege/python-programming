The file contains the steps I took to create the app on a linux run machine.


## Step 1: Install Python
1. Django requires Python 3. Ensure you have it installed. Check your Python version:
   bash
2. python3 --version
   If not installed, update your package list and install Python:
   bash
3. sudo apt update
4. sudo apt install python3 python3-pip python3-venv

## Step 2: Set Up a Virtual Environment
Using a virtual environment isolates your project dependencies.

Navigate to your desired project directory:
bash
1. mkdir my_django_project && cd my_django_project
2. Create a virtual environment:
   bash
   python3 -m venv venv
3. Activate the virtual environment:
   bash
   source venv/bin/activate
   Your terminal prompt should change, indicating the virtual environment is active.

## Step 3: Install Django
Install Django using pip:

bash
1. pip install django
   Confirm the installation:
   bash
2. django-admin --version

## Step 4: Create a Django Project
Use django-admin to create your project:

bash
1. django-admin startproject myproject .
   This will create a directory structure like:

my_django_project/
│
├── manage.py
├── myproject/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py

## Step 5: Run the Development Server
Start the development server to ensure everything works:

bash
1. python manage.py runserver
   Visit http://127.0.0.1:8000/ in your browser. You should see the "It worked!" Django welcome page.

## Step 6: Create a Django App
Apps in Django handle specific functionality (e.g., blog, authentication).

1. Create an app:
   bash
   python manage.py startapp myfirstapp
2. Register the app in myproject/settings.py:
    INSTALLED_APPS = [
    'myfirstapp',
   ]

## Step 7: Set Up the Database
1. Open myproject/settings.py and configure the database settings (SQLite is the default).
2. Apply migrations to set up the database schema:
   bash
3. python manage.py migrate

## Step 8: Create a Superuser
1. Create an admin user to access the Django admin panel:
   bash
2. python manage.py createsuperuser
3. Follow the prompts to set a username, email, and password.

## Step 9: Define Models
1. Open myfirstapp/models.py and define a model:
write the following code into it:

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
2. Apply the model migrations:
   bash
   python manage.py makemigrations
   python manage.py migrate
   
## Step 10: Use the Django Admin
1. Register the model in myfirstapp/admin.py:
   python

from django.contrib import admin
from .models import Post

admin.site.register(Post)

2. Start the server and log in to the admin panel at http://127.0.0.1:8000/admin/ using your superuser credentials.

## Step 11: Create Views and URLs
1. Open myfirstapp/views.py and define a view:
   python

   from django.http import HttpResponse

   def home(request):
      return HttpResponse("Welcome to My Django App!")
   
2. Create a URL mapping in myfirstapp/urls.py:
   python
 
   from django.urls import path
   from . import views

   urlpatterns = [
      path('', views.home, name='home'),
   ]
   
3. Include the app’s URLs in the project’s urls.py:
   python

   from django.contrib import admin
   from django.urls import path, include

   urlpatterns = [
     path('admin/', admin.site.urls),
     path('', include('myfirstapp.urls')),
   ]
   
## Step 12: Start Developing!
   Now you're set to develop your app further. Here are some next steps:

   Create templates for dynamic HTML rendering.
   Use Django’s forms for input handling.
   Add static files like CSS and JavaScript.
   Explore Django's ORM for database interactions.

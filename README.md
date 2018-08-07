# Django-for-celery

##basic explanation of each python file in django
-manage.py -> command-line utility
-mysite/ -> directory where python package sits in
-mysite/__init__.py -> directory should be considered a python package
-mysite/urls.py -> URL declarations for project
-mysite/wsgi.py -> WSGI-compatible web servers to serve project

##Django app part 1
-created an application called 'Polls'
-The app only contains views.py which outputs "Helloworld this is polls.index.views"

-The connection needs to be made with application and a project!
1. mysite/urls.py
```
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
	path('polls/', include('polls.urls')),
	path('admin/', admin.site.urls),
]
```
-the include function cuts out whatever the URL matched up to that point and send the remaining string to the include URLconf for further processing

2. polls/urls.py
```
from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
]
```
-Now, since we dont have anything further than polls/, we just merely go into this file and run views.index which just returns "helloworld!"

##Django app part 2
-settings need to be fixed but we are using SQLlite so no need to change
-model classes created(Question, Choice)
-Now we can activate the models by creating a database schema(CREATE TABLE statements) for the app
==> $python manage.py makemigrations (you can include app name here or not will run everything)
==? $python manage.py migrate

This creates a database(table) for the models we created and now we can manually create the data via python manage.py shell
-> q = Question(question_text='whats up?'...)
-> q.save()#saves the data

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
...
-> Question.objects.all()# displays how many questions object saved in db.

Now you can implement this since the output looks something like the following
 -> <Question: Question object(1)>
 -> this does not help so you can add __Str__ function in each model classes to return itself's text!

**Important note regarding DB**
-> ForeinKey tells the class that it is attached(can access) to the class of the first argument followed by the ForeignKey function.
For example, c = q.choice_set.create(...) Even though, c is not directly related to class Question, we can access it since choice has a question as a ForeignKey to Choice. c.quesiton -> <Queryset: what's up?>

Another thing is to create superuser and this is done by createsuperuser in manage.py.

##Django app part 3
Now connect the views to the application!
1. begin from the URL
-in urlpatterns, with '<int:question_id>', we pass in this integer type to views.detail or other functions. This way, we can connect the URL with views.

2. fix the views
-It is important to get the queryset and we learned how to because we are saving that queryset into a database
-How about putting them on the views?
-render() takes the request object as its first argument, a template name as its second argument and a dictionary as its optional third argument. It returns an HttpResponse object of the given template rendered with the given context.
-now, we are able to get the views connected to .html file which will render the views in terms of the .html file.

##Django app part 4
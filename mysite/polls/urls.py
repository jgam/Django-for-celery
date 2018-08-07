from django.contrib import admin
from django.urls import include, path

from . import views

app_name = 'polls'
urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('<int:pk>/', views.DetailView.as_view(), name='detail'),
	path('<int:pk>/results/', views.ResultsView.as_view(), name='reuslts'),
	path('<int:question_id>/vote/', views.vote, name='vote'),
]
"""
urlpatterns = [
	path('', views.index, name='index'),
	path('<int:question_id>/', views.detail, name='detail'),# /polls/5/
	path('<int:question_id>/results/', views.results, name='results'),
	path('<int:question_id>/vote/', views.vote, name='vote'),#/polls/5/vote/
]
"""

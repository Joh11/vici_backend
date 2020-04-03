from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_company/', views.create_company, name='create_company')]

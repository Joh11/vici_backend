from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_company/', views.create_company, name='create_company'),
    path('details/<int:company_id>/', views.details, name='details'),
    path('all_companies/', views.all_companies, name='all_companies')]

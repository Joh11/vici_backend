from django.urls import path, include
from tastypie.api import Api

from .resources import ServiceResource, CompanyResource
from . import views

app_name = 'viciapp'

v1_api = Api(api_name='v1')
v1_api.register(ServiceResource())
v1_api.register(CompanyResource())

urlpatterns = [
    path('', views.index, name='index'),
    path('create_company/', views.create_company, name='create_company'),
    path('details/<int:company_id>/', views.details, name='details'),
    path('all_companies/', views.all_companies, name='all_companies'),
    path('create_account/', views.create_account, name='create_account'),
    path('register_account/', views.register_account, name='register_account'),
    path('api/', include(v1_api.urls))]

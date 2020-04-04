from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from tastypie.api import NamespacedApi

from .resources import ServiceResource, ImageResource, CompanyResource, CommentResource
from . import views

app_name = 'viciapp'

v1_api = NamespacedApi(api_name='v1', urlconf_namespace=app_name)
v1_api.register(ServiceResource())
v1_api.register(ImageResource())
v1_api.register(CompanyResource())
v1_api.register(CommentResource())

urlpatterns = [
    path('', views.index, name='index'),

    path('accounts/', include('django.contrib.auth.urls')),
    
    path('create_company/', views.create_company, name='create_company'),
    path('details/<int:company_id>/', views.details, name='details'),
    path('all_companies/', views.all_companies, name='all_companies'),
    path('create_account/', views.create_account, name='create_account'),
    path('register_account/', views.register_account, name='register_account'),
    path('api/', include(v1_api.urls))] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

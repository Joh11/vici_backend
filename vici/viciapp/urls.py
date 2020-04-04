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
    path('login/', views.login_view, name='login'),
    path('login_process/', views.login_process, name='login_process'),
    path('file_upload/', views.file_upload, name='file_upload'),
    path('file_upload_process/', views.file_upload_process, name='file_upload_process'),
    path('api/', include(v1_api.urls))] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

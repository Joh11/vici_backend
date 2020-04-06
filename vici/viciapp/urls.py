from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from tastypie.api import NamespacedApi

from .resources import ServiceResource, ImageResource, CompanyResource, CommentResource, ApiKeyResource, UserResource
from . import views

app_name = 'viciapp'

v1_api = NamespacedApi(api_name='v1', urlconf_namespace=app_name)
v1_api.register(ServiceResource())
v1_api.register(UserResource())
v1_api.register(ImageResource())
v1_api.register(CompanyResource())
v1_api.register(CommentResource())
v1_api.register(ApiKeyResource())

urlpatterns = [
    # Main pages
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout, name='logout'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    # Processing pages
    path('login_process/', views.login_process, name='login_process'),
    # path('edit_profile_process/', views.edit_profile_process, name='edit_profile_process'),

    # Api
    path('login_app/', views.login_app, name='login_app'),
    path('sign_up_app/', views.sign_up_app, name='sign_up_app'),
    path('api/', include(v1_api.urls))] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

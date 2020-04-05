from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from tastypie import fields
from tastypie.resources import NamespacedModelResource
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from tastypie.http import HttpForbidden, HttpUnauthorized
from tastypie.models import ApiKey
from tastypie.authentication import BasicAuthentication


from .serializer import CamelCaseJSONSerializer
from .models import Company, Image, Service, Comment

class CompanyResource(NamespacedModelResource):
    services = fields.ToManyField('viciapp.resources.ServiceResource', 'services')
    comments = fields.ToManyField('viciapp.resources.CommentResource', 'comments')
    images = fields.ToManyField('viciapp.resources.ImageResource', 'images', full=True)
    
    class Meta:
        queryset = Company.objects.all() # TODO for now send all companies
        serializer = CamelCaseJSONSerializer()

class ImageResource(NamespacedModelResource):
    class Meta:
        queryset = Image.objects.all()
        serializer = CamelCaseJSONSerializer()

        
class ServiceResource(NamespacedModelResource):
    company = fields.ForeignKey(CompanyResource, 'company')
    
    class Meta:
        queryset = Service.objects.all()
        excludes = ['id']
        serializer = CamelCaseJSONSerializer()

class CommentResource(NamespacedModelResource):
    company = fields.ForeignKey(CompanyResource, 'company')
    class Meta:
        queryset = Comment.objects.all()
        serializer = CamelCaseJSONSerializer()

class ApiKeyResource(NamespacedModelResource):
    """A resource to return the API key to the mobile app from username
    and password"""
    class Meta:
        queryset = ApiKey.objects.all() # TODO something else
        # fields = ['key']
        # detail_allowed_methods = []
        # list_allowed_methods = ['get']
        authentication = BasicAuthentication()

    def login(self, request, **kwargs):
        self.method_check(request, allowed=['post'])
        return self.create_response(request, {
                    'success': True
                })

        data = self.deserialize(request, request.raw_post_data, format=request.META.get('CONTENT_TYPE', 'application/json'))

        username = data.get('username', '')
        password = data.get('password', '')

        user = authenticate(username=username, password=password)
        if user:
            return self.create_response(request, {
                    'success': True
                })
        else:
            return self.create_response(request, {
                    'success': True
                })

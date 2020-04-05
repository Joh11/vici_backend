from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout

from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance

from tastypie import fields
from tastypie.resources import NamespacedModelResource
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from tastypie.http import HttpForbidden, HttpUnauthorized
from tastypie.models import ApiKey
from tastypie.authentication import BasicAuthentication


from .serializer import CamelCaseJSONSerializer
from .models import Company, AdressPart, Image, Service, Comment

class CompanyResource(NamespacedModelResource):
    services = fields.ToManyField('viciapp.resources.ServiceResource', 'services', full=True)
    comments = fields.ToManyField('viciapp.resources.CommentResource', 'comments')
    adress_parts = fields.ToManyField('viciapp.resources.AdressPartResource', 'adress_parts', full=True)
    images = fields.ToManyField('viciapp.resources.ImageResource', 'images', full=True)
    
    class Meta:
        queryset = Company.objects.all() # TODO for now send all companies
        serializer = CamelCaseJSONSerializer()
        excludes = ['id']
        filtering = {'category': ALL,}

    def build_filters(self, filters=None):
        if filters is None:
            filters = {}
        orm_filters = super(CompanyResource, self).build_filters(filters)
        
        if 'lng' in filters and 'lat' in filters and 'r' in filters:
            lng = float(filters['lng'])
            lat = float(filters['lat'])
            r = float(filters['r'])

            point = Point(lng, lat, srid=4326)
            
            print('lng, lat, r = {},{},{}'.format(lng, lat, r))
            qset = (Q(location__distance_lte=(point, Distance(km=r))))
            
            orm_filters.update({'custom': qset})

        return orm_filters
    
    def apply_filters(self, request, applicable_filters):
        if 'custom' in applicable_filters:
            custom = applicable_filters.pop('custom')
        else:
            custom = None
            
        semi_filtered = super(CompanyResource, self).apply_filters(request, applicable_filters)

        return semi_filtered.filter(custom) if custom else semi_filtered

class AdressPartResource(NamespacedModelResource):
    class Meta:
        queryset = AdressPart.objects.all()
        serializer = CamelCaseJSONSerializer()
        
class ImageResource(NamespacedModelResource):
    class Meta:
        queryset = Image.objects.all()
        serializer = CamelCaseJSONSerializer()
        excludes = ['id']
        
class ServiceResource(NamespacedModelResource):
    company = fields.ForeignKey(CompanyResource, 'company')
    
    class Meta:
        queryset = Service.objects.all()
        excludes = ['id']
        serializer = CamelCaseJSONSerializer()

class CommentResource(NamespacedModelResource):
    company = fields.ForeignKey(CompanyResource, 'company')
    class Meta:
        excludes = ['id']
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

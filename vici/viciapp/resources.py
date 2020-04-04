from tastypie import fields
from tastypie.resources import NamespacedModelResource
from tastypie.constants import ALL, ALL_WITH_RELATIONS

from .models import Company, Service, Comment

class CompanyResource(NamespacedModelResource):
    services = fields.ToManyField('viciapp.resources.ServiceResource', 'services')
    comments = fields.ToManyField('viciapp.resources.CommentResource', 'comments')
    
    class Meta:
        queryset = Company.objects.all() # TODO for now send all companies

        
class ServiceResource(NamespacedModelResource):
    company = fields.ForeignKey(CompanyResource, 'company')
    
    class Meta:
        queryset = Service.objects.all()
        excludes = ['id']

class CommentResource(NamespacedModelResource):
    company = fields.ForeignKey(CompanyResource, 'company')
    class Meta:
        queryset = Comment.objects.all()

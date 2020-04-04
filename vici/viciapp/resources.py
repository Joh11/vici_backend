from tastypie import fields
from tastypie.resources import ModelResource
from .models import Company, Service

class CompanyResource(ModelResource):
    services = fields.ToManyField('viciapp.resources.ServiceResource', 'services')
    
    class Meta:
        queryset = Company.objects.all() # TODO for now send all companies

        
class ServiceResource(ModelResource):
    company = fields.ForeignKey(CompanyResource, 'company')
    
    class Meta:
        queryset = Service.objects.all()

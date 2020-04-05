from django.contrib.gis import admin

from .models import Company, AdressPart, Image, Service, User, Comment

# Register your models here.

current_admin = admin.OSMGeoAdmin

admin.site.register(Company, current_admin)
admin.site.register(AdressPart, current_admin)
admin.site.register(Image, current_admin)
admin.site.register(Service, current_admin)
admin.site.register(Comment, current_admin)

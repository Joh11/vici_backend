from django.contrib.gis import admin

from .models import Company, Image, Service, User, Comment

# Register your models here.

current_admin = admin.OSMGeoAdmin

admin.site.register(Company, current_admin)
admin.site.register(Image, current_admin)
admin.site.register(Service, current_admin)
admin.site.register(Comment, current_admin)

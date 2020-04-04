from django.contrib.gis import admin

from .models import Company, Image, Service, User, Comment

# Register your models here.

admin.site.register(Company, admin.GeoModelAdmin)
admin.site.register(Image, admin.GeoModelAdmin)
admin.site.register(Service, admin.GeoModelAdmin)
admin.site.register(Comment, admin.GeoModelAdmin)

from django.contrib import admin

from .models import Company, Image, Service, User, Comment

# Register your models here.

admin.site.register(Company)
admin.site.register(Image)
admin.site.register(Service)
admin.site.register(User)
admin.site.register(Comment)

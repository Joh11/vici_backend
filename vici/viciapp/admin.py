from django.contrib import admin

from .models import Company, User, Comment

# Register your models here.

admin.site.register(Company)
admin.site.register(User)
admin.site.register(Comment)

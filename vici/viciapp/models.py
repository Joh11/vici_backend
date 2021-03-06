from django.contrib.gis.db import models
from django.contrib.auth.models import User

from tastypie.models import create_api_key

from .image import compress_under_size

# Generate an API key every time a User is created
models.signals.post_save.connect(create_api_key, sender=User)

class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='company')
    
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.PointField(null=True)
    category = models.IntegerField()
    help_message = models.TextField(blank=True)

    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    
    opening_hours = models.CharField(max_length=400, blank=True)

    def __str__(self):
        return self.name

# Image handling
# Images will be saved in media/<company_id>/
def upload_image_dir_path(instance, filename):
    return 'company_{}/{}'.format(instance.company_id, filename)

class Image(models.Model):
    # Relations
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='images')
    
    # Fields
    legend = models.CharField(max_length=200)
    image = models.ImageField(upload_to=upload_image_dir_path)
    
    def save(self, *args, **kwargs):
        instance = super(Image, self).save(*args, **kwargs)
        # image = PIL.Image.open(self.image.path)
        print('Compressing images ...')
        # image.save(self.image.path, quality=20, optimize=True)
        compress_under_size(400*1000, self.image.path)
        return instance
            

    def __str__(self):
        return "Image : " + self.legend

class Contact(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='contacts')
    data = models.CharField(max_length=200)
    
class Service(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='services')
    
    category = models.IntegerField()
    description = models.TextField()
    
class Comment(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(default=5)
    message = models.TextField()

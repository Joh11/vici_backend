from django.contrib.gis.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='company')
    
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.PointField(null=True)
    category = models.IntegerField()
    help_message = models.TextField()

    opening_hours = models.CharField(max_length=400)
    adress = models.CharField(max_length=400)

    # TODO add category
    # TODO add the rest
    # TODO add position

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

    def __str__(self):
        return "Image : " + self.legend

class Contact(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='contacts')
    data = models.CharField(max_length=200)
    
class Service(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='services')
    
    logo = models.CharField(max_length=50) # TODO régler ça
    description = models.TextField()
    
class Comment(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(default=5)
    message = models.TextField()

from django.contrib.gis.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    help = models.TextField()

    location = models.PointField(null=True)
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

class Service(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='services')
    
    name = models.CharField(max_length=200)
    logo = models.CharField(max_length=50) # TODO régler ça
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    
class Comment(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(default=5)
    message = models.TextField()

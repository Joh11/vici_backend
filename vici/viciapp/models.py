from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    # TODO add category
    # TODO add images and the rest
    # TODO add position

    def __str__(self):
        return self.name

class Image(models.Model):
    # Relations
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    
    # Fields
    legend = models.CharField(max_length=200)
    image = models.ImageField()

    def __str__(self):
        return "Image : " + self.legend

class User(models.Model):
    pass # TODO see what we put here

class Comment(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(default=5)
    message = models.TextField()

from django.db import models

# Create your models here.

class News(models.Model):

    title = models.CharField(max_length=200)
    date_created =  models.DateField(auto_now=True)
    content = models.TextField(max_length=2000)
    image1 = models.ImageField(upload_to='gallery', null=True, blank=True)
    image2 = models.ImageField(upload_to='gallery', null=True, blank=True)
    image3 = models.ImageField(upload_to='gallery', null=True, blank=True)
    image4 = models.ImageField(upload_to='gallery', null=True, blank=True)

    def __str__(self):
        return self.title

class Slides1(models.Model):
    image1 = models.ImageField(upload_to='slides', null=True, blank=True)

class Slides2(models.Model):
    image2= models.ImageField(upload_to='slides', null=True, blank=True)

class Slides3(models.Model):
    image3 = models.ImageField(upload_to='slides', null=True, blank=True)

class Slides4(models.Model):
    image4 = models.ImageField(upload_to='slides', null=True, blank=True)
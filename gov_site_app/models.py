from django.db import models

# Create your models here.

class SewaHaru(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(max_length=60)
    image1 = models.ImageField(upload_to='images',null=True,blank=True)
    image2 = models.ImageField(upload_to='images',null=True,blank=True)
    image3 = models.ImageField(upload_to='images',null=True,blank=True)
    image4 = models.ImageField(upload_to='images',null=True,blank=True)
    image5 = models.ImageField(upload_to='images',null=True,blank=True)

class SuchanaItems(models.Model):
    heading = models.CharField(max_length=32,default="Title")
    suchana_photo_name = models.CharField(max_length=32)
    suchana_photo_description = models.TextField(max_length=200)
    suchana_photo = models.ImageField(upload_to='suchana',null=True,blank=True)

class PhotoGallery(models.Model):
    image1 = models.ImageField(upload_to='images',null=True,blank=True)
    descriptionOfImage1 = models.TextField(max_length=200,default="Title")
    image2 = models.ImageField(upload_to='images',null=True,blank=True)
    descriptionOfImage2 = models.TextField(max_length=200,default="Title")
    image3 = models.ImageField(upload_to='images',null=True,blank=True)
    descriptionOfImage3 = models.TextField(max_length=200,default="Title")
    image4 = models.ImageField(upload_to='images',null=True,blank=True)
    descriptionOfImage4 = models.TextField(max_length=200,default="Title")
    image5 = models.ImageField(upload_to='images',null=True,blank=True)
    descriptionOfImage5 = models.TextField(max_length=200,default="Title")    

class Headline(models.Model):
        headline_topic = models.TextField(max_length=2000)
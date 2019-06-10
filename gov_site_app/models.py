from django.db import models


# Create your models here.

class SuchanaItems(models.Model):
    Suchana1_heading = models.CharField(max_length=32, default="Title")
    Suchana1_suchana_photo_name = models.CharField(max_length=32,null=True, blank=True,default="Title")
    Suchana1_suchana_photo_description = models.TextField(max_length=200,null=True, blank=True,default="Title")
    Suchana1_suchana_photo = models.ImageField(upload_to='suchana', null=True, blank=True,default="Title")
    Suchana2_heading = models.CharField(max_length=32, default="Title")
    Suchana2_suchana_photo_name = models.CharField(max_length=32,null=True, blank=True,default="Title")
    Suchana2_suchana_photo_description = models.TextField(max_length=200,null=True, blank=True,default="Title")
    Suchana2_suchana_photo = models.ImageField(upload_to='suchana', null=True, blank=True)
    Suchana3_heading = models.CharField(max_length=32,null=True, blank=True, default="Title")
    Suchana3_suchana_photo_name = models.CharField(max_length=32,null=True, blank=True, default="Title")
    Suchana3_suchana_photo_description = models.TextField(max_length=200,null=True, blank=True, default="Title")
    Suchana3_suchana_photo = models.ImageField(upload_to='suchana', null=True, blank=True)


class PhotoGallery(models.Model):
    image1 = models.ImageField(upload_to='images', null=True, blank=True)
    descriptionOfImage1 = models.TextField(max_length=200, default="Title")
    image2 = models.ImageField(upload_to='images', null=True, blank=True)
    descriptionOfImage2 = models.TextField(max_length=200, default="Title")
    image3 = models.ImageField(upload_to='images', null=True, blank=True)
    descriptionOfImage3 = models.TextField(max_length=200, default="Title")
    image4 = models.ImageField(upload_to='images', null=True, blank=True)
    descriptionOfImage4 = models.TextField(max_length=200, default="Title")
    image5 = models.ImageField(upload_to='images', null=True, blank=True)
    descriptionOfImage5 = models.TextField(max_length=200, default="Title")


class Headline(models.Model):
    headline_topic = models.TextField(max_length=2000)



class OrganizationDetail(models.Model):
    phone = models.TextField(max_length=20)
    email = models.TextField(max_length=100)
    website = models.TextField(max_length=100)


class GaupalikaBare(models.Model):
    jesthaNagarik = models.TextField(max_length=20)
    dalit = models.TextField(max_length=100)
    bidhuwa = models.TextField(max_length=100)
    aakal_mahila = models.TextField(max_length=100)
    aapanga = models.TextField(max_length=100)
    dalit = models.TextField(max_length=100)
    balbalika = models.TextField(max_length=100)
    balbalika = models.TextField(max_length=100)
    jamma = models.TextField(max_length=100)

from django.shortcuts import render
from django.http import HttpResponse
from gov_site_app.models import SewaHaru,SuchanaItems,PhotoGallery,Headline
# Create your views here.

def index(request):
    image_list = SewaHaru.objects.all()
    suchana_list = SuchanaItems.objects.all()
    photogallery_list = PhotoGallery.objects.all()
    headline_list = Headline.objects.all()
    return render(request,'gov_site_app/gov_site_main.html',{"suchana_items":suchana_list,"images":image_list,"photo_gallery_images":photogallery_list,"headline":headline_list})



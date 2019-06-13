from django.shortcuts import render
from gov_site_app.models import SuchanaItems, PhotoGallery, Headline, OrganizationDetail, GaupalikaBare, Janapratinidhi


# Create your views here.

def index(request):
    suchana_list = SuchanaItems.objects.all()
    photogallery_list = PhotoGallery.objects.all()
    headline_list = Headline.objects.all()
    organization_detail = OrganizationDetail.objects.all().first()
    gaupalika_detail = GaupalikaBare.objects.all().first()
    Janapratinidhi_detail = Janapratinidhi.objects.all()
    return render(request, 'gov_site_app/gov_site_main.html'
                  , {"suchana_items": suchana_list,
                     "photo_gallery_images": photogallery_list,
                     "headline": headline_list,
                     "organization_detail": organization_detail,
                     "gaupalika_info": gaupalika_detail,
                     "janapratinidhi_info": Janapratinidhi_detail
                     })

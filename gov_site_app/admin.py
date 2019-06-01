from django.contrib import admin
from gov_site_app.models import SuchanaItems, PhotoGallery, Headline, OrganizationDetail, GaupalikaBare

# Register your models here.
admin.site.register(SuchanaItems)
admin.site.register(PhotoGallery)
admin.site.register(Headline)
admin.site.register(OrganizationDetail)
admin.site.register(GaupalikaBare)

admin.site.site_header = 'Gaupalika Database'

from django.contrib import admin
from gov_site_app.models import Sewa,SuchanaItems, PhotoGallery, Headline, OrganizationDetail, GaupalikaBare, Janapratinidhi


class HeadlineAdmin(admin.ModelAdmin):
    list_display = ('id', 'headline_topic',)
    list_editable = ('headline_topic',)

    def has_add_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return False

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save_and_add_another'] = False
        extra_context['show_save'] = True

        return super(HeadlineAdmin, self).changeform_view(request, object_id, extra_context=extra_context)


class SuchanaItemsAdmin(admin.ModelAdmin):

    def has_add_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return False

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save_and_continue'] = False
        extra_context['show_save'] = True

        return super(SuchanaItemsAdmin, self).changeform_view(request, object_id, extra_context=extra_context)


class PhotoGalleryAdmin(admin.ModelAdmin):

    def has_add_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return False

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}

        extra_context['show_save_and_continue'] = False
        extra_context['show_save_and_add_another'] = False
        extra_context['show_save'] = True

        return super(PhotoGalleryAdmin, self).changeform_view(request, object_id, extra_context=extra_context)


class JanapratinidhiAdmin(admin.ModelAdmin):

    def has_add_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return False

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save_and_continue'] = False
        extra_context['show_save_and_add_another'] = False
        extra_context['show_save'] = True

        return super(JanapratinidhiAdmin, self).changeform_view(request, object_id, extra_context=extra_context)


class GaupalikaBareAdmin(admin.ModelAdmin):

    def has_add_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return False

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save_and_continue'] = False
        extra_context['show_save_and_add_another'] = False
        extra_context['show_save'] = True

        return super(GaupalikaBareAdmin, self).changeform_view(request, object_id, extra_context=extra_context)


class OrganizationDetailAdmin(admin.ModelAdmin):

    def has_add_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return False

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save_and_continue'] = False
        extra_context['show_save_and_add_another'] = False
        extra_context['show_save'] = True

        return super(OrganizationDetailAdmin, self).changeform_view(request, object_id, extra_context=extra_context)



admin.site.register(SuchanaItems, SuchanaItemsAdmin)
admin.site.register(PhotoGallery, PhotoGalleryAdmin)
admin.site.register(Headline, HeadlineAdmin)
admin.site.register(OrganizationDetail, OrganizationDetailAdmin)
admin.site.register(GaupalikaBare, GaupalikaBareAdmin)
admin.site.register(Janapratinidhi, JanapratinidhiAdmin)
admin.site.register(Sewa)

# class ListingAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'is_published',
#                     'price', 'list_date', 'realtors')
#     list_display_links = ('id', 'title')
#     list_filter = ('realtors',)
#     list_editable = ('is_published',)
#     search_fields = ('title', 'description', 'address',
#                      'city', 'state', 'zipcode', 'price')
#     list_per_page = 25
# admin.site.register(Listing, ListingAdmin)

from django.contrib import admin
from .models import Listing

class ActiveListingAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).filter(is_active=True)

class InactiveListingAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).filter(is_active=False)

class ActiveListing(Listing):
    class Meta:
        proxy = True
        verbose_name = '✅ Active Listing'
        verbose_name_plural = '✅ Active Listings'

class InactiveListing(Listing):
    class Meta:
        proxy = True
        verbose_name = '⏸️ Paused Listing'
        verbose_name_plural = '⏸️ Paused Listings'

admin.site.register(ActiveListing, ActiveListingAdmin)
admin.site.register(InactiveListing, InactiveListingAdmin)
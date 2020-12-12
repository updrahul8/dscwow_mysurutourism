from django.conf import settings
from django.contrib import admin
from tour.models import Place, Category,  Event

# Register your models here.
admin.site.register(Category),
admin.site.register(Event),

#django google maps 
@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

    fieldsets = (
        (None, {
            'fields': ( 'name', 'place_description', 'place_img_1', 'place_img_2', 'place_img_3', 'place_category', 'place_location', 'latitude', 'longitude',)
        }),
    )

    class Media:
        if hasattr(settings, 'GOOGLE_MAPS_API_KEY') and settings.GOOGLE_MAPS_API_KEY:
            css = {
                'all': ('css/admin/location_picker.css',),
            }
            js = (
                'https://maps.googleapis.com/maps/api/js?key={}'.format(settings.GOOGLE_MAPS_API_KEY),
                'js/admin/location_picker.js',
            )
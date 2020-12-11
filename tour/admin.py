from django.contrib import admin
from tour.models import Place, Category,  Event

# Register your models here.
admin.site.register(Place),
admin.site.register(Category),
admin.site.register(Event),
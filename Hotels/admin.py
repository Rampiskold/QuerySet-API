from django.contrib import admin
from .models import *


class HotelAdmin(admin.ModelAdmin):
    list_display = ["id","title"]
    # search_fields = [field.name for field in Hotel._meta.fields]

    class Meta:
        model = Hotel


admin.site.register(Hotel, HotelAdmin)


class RegionAdmin(admin.ModelAdmin):
    list_display = ["id","title"]
    # search_fields = [field.name for field in Region._meta.fields]

    class Meta:
        model = Region


admin.site.register(Region, RegionAdmin)

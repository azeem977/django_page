from django.contrib import admin
from django.utils.html import format_html
from .models import FruitType


@admin.register(FruitType)
class FruitTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added', 'image_tag')  # show thumbnail

    def image_tag(self, obj):
        if obj.image:   
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover;"/>', obj.image.url)
        return "-"
    image_tag.short_description = 'Image'  

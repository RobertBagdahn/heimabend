from django.contrib import admin
from .models import Tag, Event, TagCategory, Event, Image, Material


admin.site.register(Event)
admin.site.register(TagCategory)
admin.site.register(Tag)
admin.site.register(Image)
admin.site.register(Material)

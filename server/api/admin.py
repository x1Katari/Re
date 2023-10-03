from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Title, Volume, Chapter, Tag

admin.site.register(Volume)
admin.site.register(Chapter)
admin.site.register(Tag)


@admin.register(Title)
class TitleAdmin(ModelAdmin):
    search_fields = ['rus_name']

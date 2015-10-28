from django.contrib import admin
from.models import *

class PhotoInline(admin.StackedInline):
    model = Photo

class AlbumAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]

admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo)

# Register your models here.

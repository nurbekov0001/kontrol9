from django.contrib import admin
from webapp.models import Photo, Album, Chosen

class PhotosAdmin(admin.ModelAdmin):
    list_display = ['id', 'the_photo', 'signature', 'author', 'created_at', 'choice', 'album']
    list_filter = ['author']
    fields = ['the_photo', 'signature', 'author', 'choice']

class AlbumsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'author', 'created_at', 'choice']
    list_filter = ['author']
    fields = ['name', 'description', 'author', 'choice']

class ChosenAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo_id', 'user_id']


admin.site.register(Photo, PhotosAdmin)
admin.site.register(Album, AlbumsAdmin)
admin.site.register(Chosen, ChosenAdmin)

# Register your models here.

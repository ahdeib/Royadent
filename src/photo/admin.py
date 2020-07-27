from .models import Album, AlbumImage
from django.contrib import admin

class AlbumModelAdmin(admin.ModelAdmin):
    
    list_display = ('title', 'albums_covers')
    list_filter = ('created',)

class AlbumImageModelAdmin(admin.ModelAdmin):
    list_display = ('image', 'created' )
    list_filter = ('album', 'created')

admin.site.register(Album, AlbumModelAdmin)
admin.site.register(AlbumImage, AlbumImageModelAdmin)
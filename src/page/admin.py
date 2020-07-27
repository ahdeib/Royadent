from .models import Page
from django.contrib import admin


# Register your models here.

class PageAdmin(admin.ModelAdmin):  # instead of ModelAdmin

    list_display = ['title' ,'author', 'active', 'created_date']
    search_fields = ['title', 'content' ]
    list_filter = ('title','author')


admin.site.register(Page, PageAdmin)
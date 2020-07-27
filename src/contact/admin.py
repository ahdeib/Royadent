from .models import Contact
from django.contrib import admin


# Register your models here.

class ContactAdmin(admin.ModelAdmin):  # instead of ModelAdmin

    list_display = ['contact_title' ,'author', 'created_date']
    search_fields = ['contact_title', 'content' ]
    list_filter = ('contact_title','author')


admin.site.register(Contact, ContactAdmin)
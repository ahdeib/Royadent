from django.contrib import admin

# Register your models here.
from .models import Service , Category , ServiceImages

admin.site.register(Service)
admin.site.register(Category)
admin.site.register(ServiceImages)

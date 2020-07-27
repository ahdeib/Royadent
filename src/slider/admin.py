from .models import Slider
from django.contrib import admin

class SliderModelAdmin(admin.ModelAdmin):

    list_display = ('title', 'image')
    list_filter = ('created',)


admin.site.register(Slider, SliderModelAdmin)
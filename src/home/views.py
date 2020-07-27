from django.shortcuts import render
from page.models import Page
from slider.models import Slider
from contact.models import Contact
#from django.core.paginator import Paginator

# Create your views here.


def main_home(request):
    
    slider_data = Slider.objects.all()
    
    
  
    

    context = {
        'slider_data' : slider_data,
    }

    return render(request , 'home/index.html', context)
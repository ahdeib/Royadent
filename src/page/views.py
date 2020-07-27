from django.shortcuts import render
from .models import Page
# Create your views here.


def page_detail(request , id):
    page_detail = Page.objects.filter(id=id)  


    context = {
        'page_detail' : page_detail ,

    }

    return render(request , 'pages/page_detail.html' , context)






from page.models import Page
from slider.models import Slider
from contact.models import Contact
from photo.models import Album, AlbumImage
from employee.models import Employee


def add_variable_to_context(request):
    slider = Slider.objects.all()
    page_about = Page.objects.filter(id=1)
    contact = Contact.objects.all()
    album_Image = AlbumImage.objects.all()
    employee = Employee.objects.all()
   
    return {
        'slider': slider,
        'contact': contact,
        'page_about':page_about,
        'album_Image':album_Image,
        'employee' : employee,
        }
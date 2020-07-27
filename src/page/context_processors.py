from page.models import Page

def add_variable_to_context(request):
    items = Page.objects.all()
   
    return {
        'items': items
        }
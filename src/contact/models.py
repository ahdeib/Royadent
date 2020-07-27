from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
#from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Contact(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    contact_title = models.TextField(max_length=45, blank=False, null=True)
    content = RichTextField(blank=True, null=True)
    address = models.TextField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    img = models.FileField(upload_to='contact_img/', default='contact_img/def.png')
    created_date = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.contact_title

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
#from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Page(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    brief = RichTextField(blank=True, null=True)
    content = RichTextField()
    #content = RichTextUploadingField()
    img = models.FileField(upload_to='page_img/', default='page_img/def.png')
    created_date = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

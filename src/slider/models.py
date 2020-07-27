from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Slider(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField(max_length=1024)
    image =  models.FileField(upload_to='slider/')
    is_visible = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title
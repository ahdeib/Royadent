from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Album(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField(max_length=1024)
    albums_covers =  models.FileField(upload_to='albums_covers/', default='albums_covers/def.png')
    is_visible = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)

    #def get_absolute_url(self):
    #    return reverse('album', kwargs={'slug':self.slug})

    def __str__(self):
       return self.title
    def __unicode__(self):
       return self.title

class AlbumImage(models.Model):
    image =  models.FileField(upload_to='albums/', default='albums/def.png')
    album = models.ForeignKey(Album, on_delete=models.PROTECT)
    is_visible = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
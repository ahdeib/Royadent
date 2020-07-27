from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# resize image 
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=250, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=250, db_index=True)
    email = models.EmailField(unique=True)
    photo = models.ImageField(upload_to='employee/')
    photo_thumbnail = ImageSpecField(source='photo',
                                      processors=[ResizeToFill(600, 600)],
                                      format='JPEG',
                                      options={'quality': 90})

    phone_number = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
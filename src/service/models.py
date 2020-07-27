from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.

class Service(models.Model):

    ## contain all the products informations
    name = models.CharField(max_length=100, verbose_name=_("Name"))
    description = RichTextField(max_length=500, verbose_name=_("Description"))
    category = models.ForeignKey('Category' , on_delete=models.SET_NULL , null=True, verbose_name=_("Category"))
    #price = models.DecimalField(max_digits=10,decimal_places=5, verbose_name=_("Price"))
    #discount_price = models.DecimalField(max_digits=10,decimal_places=5, verbose_name=_("Discount Price"))
    image = models.ImageField(upload_to='main_product/' , blank=True , null=True, verbose_name=_("Image"))
    created = models.DateTimeField(default=timezone.now, verbose_name=_("Created Date"))
    
    slug = models.SlugField(blank=True  , null=True, verbose_name=_("Slug"))
    
    def save(self , *args , **kwargs):
        if not self.slug and self.name :
            self.slug = slugify(self.name)
        super(Service , self).save(*args , **kwargs)

           
    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.name




class ServiceImages(models.Model):
    service = models.ForeignKey(Service , on_delete=models.CASCADE, verbose_name=_("Name"))
    image = models.ImageField(upload_to='service/' , blank=True , null=True, verbose_name=_("Service Image"))

    def __str__(self):
        return self.service.name

    class Meta:
        verbose_name = 'Service Image'
        verbose_name_plural = 'Service Images'




class Category(models.Model):
    ## for product category
    category_name = models.CharField(max_length=50, verbose_name=_("Category Name"))
    category_parent= models.ForeignKey('self', limit_choices_to={'category_parent__isnull': True}, verbose_name=_("category_parent"), blank=True, null=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='category/' , blank=True , null=True, verbose_name=_("Image"))

    slug = models.SlugField(blank=True  , null=True, verbose_name=_("Slug"))


    def save(self , *args , **kwargs):
        if not self.slug and self.category_name :
            self.slug = slugify(self.category_name)
        super(Category , self).save(*args , **kwargs)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name


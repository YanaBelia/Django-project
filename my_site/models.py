from django.db import models
from django.urls import reverse

class Product(models.Model):
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to = 'photos', blank = True, null = True)
    slug = models.SlugField(verbose_name='URL', max_length=50, unique=True,default='default')
    content = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    time_create = models.DateTimeField(auto_now_add=True, null=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    type = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('my_site:product_detail', kwargs={'id':self.id, 'slug': self.slug})

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(verbose_name='URL', max_length=50, unique=True,default='default')
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('my_site:category', kwargs={'type_id': self.id})

from django.contrib import admin
from django import forms
# Register your models here.
from .models import Product, Category
from cart.models import Order
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title", )}
    list_display = ('title', 'type', 'price')
    list_filter = ('title', 'type')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Order)

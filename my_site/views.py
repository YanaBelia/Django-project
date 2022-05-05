from django.shortcuts import render, redirect, get_object_or_404
from django import forms

from .models import  Product, Category
from cart.forms import CartAddProductForm

def menu(request):
    context = {
        'type_selected':0,
    }
    return render(request, 'my_site/other/menu.html', context=context)


def Orders_details(request):
    product = Product.objects.all()
    context = {
        'product':product,
        'type_selected':0,
    }
    return render (request, 'my_site/other/orders.html', context=context)

def show_category(request, type_id):
        product = Product.objects.filter(type_id=type_id)
        type = Category.objects.all()

        context = {
            'product':product,
            'type':type,
            'type_selected': type_id,
        }
        return render(request, 'my_site/other/orders.html',context=context)

def product_detail(request, id,  slug):
    product=get_object_or_404(Product, id=id, slug=slug, is_published=True)
    cart_product_form = CartAddProductForm()
    context = {
        'product':product,
        'type_selected':product.type_id,
        'cart_product_form':cart_product_form,
    }
    return render(request, 'my_site/other/detail.html', context=context)

from django.shortcuts import render
from django import forms
from .models import Order
from decimal import Decimal
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from my_site.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from django.http import HttpResponse


@require_POST


def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('my_site:orders')


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'email', 'phone', 'city', 'street', 'street_number']


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],'update': True})

    q_list = list(item['quantity'] for item in cart)
    t_list = list(item['product'] for item in cart)
    order_data = zip(t_list, q_list)

    form = OrderForm(request.POST or None)
    if form.is_valid():
        form.save()
        cart.clear()
        return redirect('my_site:orders')

    return render(request, 'cart/detail.html', {'cart': cart, 'form':form, 'order_data':order_data})

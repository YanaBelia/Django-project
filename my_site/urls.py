from django.urls import path
from . import views

app_name = 'my_site'

urlpatterns = [
    path('', views.menu, name = 'menu'),
    path('orders', views.Orders_details, name='orders'),
    path('<int:id>/<slug:slug>', views.product_detail, name='product_detail'),
    path('<int:type_id>', views.show_category, name='category'),


]

from django.shortcuts import render
from django.views import generic

from .models import Products


class ProductListView(generic.ListView):
    # model = Products
    queryset = Products.objects.filter(active=True)
    template_name = 'products/products_list.html'
    context_object_name = 'products'


class ProductDetailView(generic.DetailView):
    model = Products
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

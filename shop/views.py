from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product

# def index(request):
#     products = Product.objects.all() # Query all products
#     return render(request, 'shop/index.html', {'products': products})


class ProductListView(ListView):
    model = Product
    template_name = 'shop/index.html' # Use 'shop/index.html' for listing products
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/product_detail.html'
    context_object_name = 'product'
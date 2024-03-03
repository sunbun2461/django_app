from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Product, Category

class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/product_detail.html'
    context_object_name = 'product'

class ProductListView(ListView):
    model = Product
    template_name = 'shop/index.html'
    context_object_name = 'products' 

    
class CategoryListView(ListView):
    model = Category
    template_name = 'shop/category_list.html'
    context_object_name = 'categories'

 
 
def index(request):
    return render(request, 'shop/index.html')

def category_list(request): # This function gets all the categories that have no parent
    categories = Category.objects.filter(parent=None) # This line gets all the categories that have no parent
    return render(request, 'shop/category_list.html', {'categories': categories})#the line 'categories' is a key, this is a dictionary

def category_detail(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    return render(request, 'shop/category_detail.html', {'category': category}) #the line 'category' is a key, this is a dictionary

def sub_category_detail(request):
    return render(request, 'shop/sub_category_detail.html')

def sub_category_detail(request, category_name, sub_category_name):
    sub_category = get_object_or_404(Category, name=sub_category_name, parent__name=category_name)
    products = Product.objects.filter(category=sub_category)
    return render(request, 'shop/sub_category_detail.html', {'sub_category': sub_category, 'products': products})

# Path: shop/models.py


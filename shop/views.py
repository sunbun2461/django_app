from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, Category
from django.shortcuts import get_object_or_404

class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/product_detail.html'
    context_object_name = 'product'

class ProductListView(ListView):
    model = Product
    template_name = 'shop/index.html'
    context_object_name = 'products' #what is context_object_name? #context_object_name is the name of the variable that will be used in the template to represent the list of objects
class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'

 
 
def index(request):
    return render(request, 'shop/index.html')

def category_list(request): # This function gets all the categories that have no parent
    categories = Category.objects.filter(parent=None) # This line gets all the categories that have no parent
    return render(request, 'category_list.html', {'categories': categories})#the line 'categories' is a key, this is a dictionary

def category_detail(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    return render(request, 'category_detail.html', {'category': category}) #the line 'category' is a key, this is a dictionary

def sub_category_detail(request):
    return render(request, 'shop/sub_category_detail.html')

def sub_category_detail(request, category_name, sub_category_name):
    sub_category = get_object_or_404(Category, name=sub_category_name, parent__name=category_name)
    products = Product.objects.filter(category=sub_category)
    return render(request, 'sub_category_detail.html', {'sub_category': sub_category, 'products': products})

# Path: shop/models.py


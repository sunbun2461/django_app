from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product
from .models import Category  # Add this line to import the Category model
from django.shortcuts import get_object_or_404 # Add this line to import the get_object_or_404 function

# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = 'shop/index.html' # Use 'shop/index.html' for listing products
    context_object_name = 'products'

class ProductDetailView(DetailView): # This class-based view is for the product detail page
    model = Product
    template_name = 'shop/product_detail.html'
    context_object_name = 'product'


# how are the class views and the def views different?
#   class views are used for more complex views, and def views are used for simpler views, such as the category_list and category_detail views

# why dont the def views have a corresponding class in models.py? because the def views are simpler views, and do not require a model

# what is a complex view vs a simple view?  a complex view is a view that requires more than one model, and a simple view is a view that requires only one model  
 
 

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

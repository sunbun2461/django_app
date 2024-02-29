# from .views import index, ProductListView, ProductDetailView
from django.urls import path
from .views import ProductListView, ProductDetailView, category_list, category_detail, sub_category_detail

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),  # Main shop page
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),  # Product detail page
    path('category/', category_list, name='category_list'),
    path('c/<str:category_name>/', category_detail, name='category_detail'),
    path('c/<str:category_name>/<str:sub_category_name>/', sub_category_detail, name='sub_category_detail'),
]

# from .views import index

from django.urls import path
from .views import ProductListView, ProductDetailView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),  # Main shop page
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),  # Product detail page
]
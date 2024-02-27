from django.contrib import admin
from .models import Product
from .models import Category
from django_summernote.admin import SummernoteModelAdmin

class CategoryAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)
    list_display = ('name','parent')
    list_filter = ('parent',)
    search_fields = ['name']

class ProductAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)


from django.contrib import admin
from .models import Product, Order

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'date', 'client_identifier', 'notes', 'contact_type', 'contact_handle', 'created_at')
    list_filter = ('date', 'contact_type', 'product')
    search_fields = ('client_identifier', 'contact_handle', 'notes')
    date_hierarchy = 'date'

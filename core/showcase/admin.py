from django.contrib import admin
from .models import Category, Product, Vendor, Customer, Order

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    list_filter = ['name']
    prepopulated_fields = {"slug": ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'slug', 'price', 'in_stock', 'created_at', 'updated_at']
    list_filter = ['in_stock', 'is_active']
    search_fields = ('title', 'price', 'author')
    list_editable = ['price', 'in_stock']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ['vendor_name', 'image']
    list_filter = ['category']
    search_fields = ('vendor_name', 'title')
    prepopulated_fields = {'slug': ('vendor_name',)}


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['nickname', 'slug']
    list_filter = ['nickname']
    search_fields = ['nickname']
    prepopulated_fields = {'slug': ('nickname',)}


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['product', 'vendor', 'price', 'quantity', 'status']
    list_filter = ['date', 'price']
    list_editable = ['price', 'quantity']
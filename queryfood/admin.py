from django.contrib import admin

# Register your models here.

from . import models

@admin.register(models.Product)
class ProductaAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'unit'
    ]

@admin.register(models.Cart)
class Cartadmin(admin.ModelAdmin):
    list_display = [
        'user'
    ] 

@admin.register(models.CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = [
        'cart',
        'product',
        'unit'
    ]

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'namae',
    ]

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'order_code',
        'status',
        'date'
    ]
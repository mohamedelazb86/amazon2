from django.contrib import admin

from .models import Product,Review,Image_Product,Brand

class ProductAdmin(admin.ModelAdmin):
    list_display=['name','flag','brand']
    list_filter=['flag','brand']
    search_fields=['subtitle','name','descriptions']

admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Review)
admin.site.register(Image_Product)
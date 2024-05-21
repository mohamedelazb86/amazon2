from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Product,Review,Image_Product,Brand

class Images(admin.TabularInline):
    model=Image_Product

class ProductAdmin(SummernoteModelAdmin):

    list_display=['name','flag','brand']
    list_filter=['flag','brand']
    search_fields=['subtitle','name','descriptions']

    inlines=[Images]

    summernote_fields = ('subtitle','descriptions')

admin.site.register(Product,ProductAdmin)
admin.site.register(Brand)
admin.site.register(Review)
#admin.site.register(Image_Product)
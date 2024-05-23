from django.shortcuts import render
from django.db.models.aggregates import Count
from django.views.generic import ListView,DetailView
from .models import Product,Brand,Review,Image_Product


class Product_List(ListView):
    model=Product
    template_name='product/product_list.html'
    paginate_by=12


class Product_Detail(DetailView):
    model=Product
    template_name='product/product_detail.html'


    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["reviews"] =Review.objects.filter(product=self.get_object())
        context["images"] =Image_Product.objects.filter(product=self.get_object())
        context["related"] =Product.objects.filter(brand=self.get_object().brand)
        return context
    

class Brand_list(ListView):
    model=Brand
    template_name='product/brand_list.html'
    paginate_by=20

    queryset=Brand.objects.annotate(product_count=Count('product_brand'))

class Brand_detail(DetailView):
    model=Brand
    template_name='product/brand_detail.html'

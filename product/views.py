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

# class Brand_detail(DetailView):
#     model=Brand
#     template_name='product/brand_detail.html'

#     queryset=Brand.objects.annotate(product_number=Count('product_brand'))

#     def get_context_data(self, **kwargs) :
#         context = super().get_context_data(**kwargs)
#         context["related"] = Product.objects.filter(brand=self.get_object())
#         return context


class Brand_detail(ListView):
    model=Product
    template_name='product/brand_detail.html'

    def get_queryset(self):
        brand=Brand.objects.get(slug=self.kwargs['slug'])
        queryset=super().get_queryset().filter(brand=brand)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brand"] =Brand.objects.filter(slug=self.kwargs['slug']).annotate(product_count=Count('product_brand'))[0]
        return context
    
    
    

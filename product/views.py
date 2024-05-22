from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Product


class Product_List(ListView):
    model=Product

class Product_Detail(DetailView):
    model=Product

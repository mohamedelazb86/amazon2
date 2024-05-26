from django.urls import path
from .views import Product_List,Product_Detail,Brand_detail,Brand_list
from .api import ProductDetailApi,ProductListApi,BrandDetailApi,BrandListApi


urlpatterns = [
    
    path('brands',Brand_list.as_view()),
    path('brands/<slug:slug>',Brand_detail.as_view()),

    path('',Product_List.as_view()),
    path('<slug:slug>',Product_Detail.as_view()),


    # api

    path('list/api',ProductListApi.as_view()),
    path('api/<int:pk>',ProductDetailApi.as_view()),

    path('brands/api/list',BrandListApi.as_view()),
    path('brands/api/<int:pk>',BrandDetailApi.as_view()),
]

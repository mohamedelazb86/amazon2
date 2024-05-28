from django.urls import path
from .views import Order_list,checkout

urlpatterns = [
    path('',Order_list),
    path('checkout',checkout)
]

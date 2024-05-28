from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Order

def Order_list(request):
    
    orders=Order.objects.filter(user=request.user)
    context={
        'orders':orders
    }
    return render(request,'orders/order_list.html',context)


def checkout(request):
    return render(request,'orders/checkout.html',{})
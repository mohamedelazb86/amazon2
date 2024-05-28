
from .models import Cart,Cart_Detail

def get_context_data(request):
    if request.user.is_authenticated:
        cart , created=Cart.objects.get_or_create(user=request.user,status='inprogress')
        cart_detail=Cart_Detail.objects.filter(cart=cart)
        return {'cart_data':cart,'cart_detail_data':cart_detail}
    else:
        return {}
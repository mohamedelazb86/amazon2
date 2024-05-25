from .serializers import Product_Detail_Serializers,Product_list_Serializers
from .serializers import BrandListSerializers,Brand_Detail_Serializers
from .models import Brand,Product
from rest_framework.generics import ListAPIView,RetrieveAPIView

class ProductListApi(ListAPIView):
    serializer_class=Product_list_Serializers
    queryset=Product.objects.all()

class ProductDetailApi(RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=Product_Detail_Serializers


class BrandListApi(ListAPIView):
    queryset=Brand.objects.all()
    serializer_class=BrandListSerializers


class BrandDetailApi(RetrieveAPIView):
    queryset=Brand.objects.all()
    serializer_class=Brand_Detail_Serializers


    
from rest_framework import serializers
from .models import Product,Brand

class Product_list_Serializers(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'
class Product_Detail_Serializers(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'


class BrandListSerializers(serializers.ModelSerializer):
    class Meta:
        model=Brand
        fields='__all__'

class Brand_Detail_Serializers(serializers.ModelSerializer):
    class Meta:
        model=Brand
        fields='__all__'



from rest_framework import serializers
from .models import Product,Brand,Image_Product

class ImageSerializers(serializers.ModelSerializer):
    class Meta:
        model=Image_Product
        fields='__all__'

class Product_list_Serializers(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'
class Product_Detail_Serializers(serializers.ModelSerializer):
    brand=serializers.StringRelatedField()
    images=ImageSerializers(source='imageproduct_product',many=True)
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



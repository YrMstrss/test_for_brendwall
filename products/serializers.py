from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """
    Сериалайзер продукта
    """

    class Meta:
        model = Product
        fields = '__all__'
        validators = [

        ]

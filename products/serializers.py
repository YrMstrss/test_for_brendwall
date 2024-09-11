from rest_framework import serializers

from products.models import Product
from products.validators import PriceValidator


class ProductSerializer(serializers.ModelSerializer):
    """
    Сериалайзер продукта
    """

    class Meta:
        model = Product
        fields = '__all__'
        validators = [
            PriceValidator(field='price',)
        ]

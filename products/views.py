from rest_framework import generics

from products.models import Product
from products.serializers import ProductSerializer


class ProductCreateAPIView(generics.CreateAPIView):
    """
    Контроллер для создания продукта
    """
    serializer_class = ProductSerializer


class ProductListAPIView(generics.ListAPIView):
    """
    Контроллер для получения списка продуктов
    """

    serializer_class = ProductSerializer
    queryset = Product.objects.all()

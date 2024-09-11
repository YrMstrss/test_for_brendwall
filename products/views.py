from rest_framework import generics

from products.serializers import ProductSerializer


class ProductCreateAPIView(generics.CreateAPIView):
    """
    Контроллер для создания продукта
    """
    serializer_class = ProductSerializer

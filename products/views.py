from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response


from products.models import Product
from products.serializers import ProductSerializer


class ProductCreateAPIView(generics.CreateAPIView):
    """
    Контроллер для создания продукта
    """
    serializer_class = ProductSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'product_form.html'

    def get(self, request):
        return Response()


class ProductListAPIView(generics.ListAPIView):
    """
    Контроллер для получения списка продуктов
    """

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    # renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'product_list.html'

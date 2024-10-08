from django.urls import path

from products.apps import ProductsConfig
from products.views import ProductCreateAPIView, ProductListAPIView

app_name = ProductsConfig.name

urlpatterns = [
    path('create/', ProductCreateAPIView.as_view(), name='create-product'),
    path('list/', ProductListAPIView.as_view(), name='list-product'),
]

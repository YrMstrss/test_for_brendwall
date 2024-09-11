from django.db import models


class Product(models.Model):
    """
    Модель продукта
    """
    name = models.CharField(max_length=100, verbose_name='название')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

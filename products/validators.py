from rest_framework.exceptions import ValidationError


class PriceValidator:
    """
    Валидатор для проверки цены товара (должна быть положительным числом)
    """
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_value = dict(value).get(self.field)
        if not 0 < tmp_value:
            raise ValidationError('Цена не может быть меньше 0')

from rest_framework import fields, serializers

from .models import Order


class OrdersSerializer(serializers.ModelSerializer):
    # Заказы #

    class Meta:
        model = Order
        fields = ("__all__")

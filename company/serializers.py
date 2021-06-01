from rest_framework import fields, serializers

from .models import Contacts, Shedule, Payment, Delivery, Weight


class ContactsSerializer(serializers.ModelSerializer):
    # Контакты #

    class Meta:
        model = Contacts
        fields = ("__all__")

class DeliverySerializer(serializers.ModelSerializer):
    # Виды доставок #

    class Meta:
        model = Delivery
        fields = ("__all__")

class PaymentSerializer(serializers.ModelSerializer):
    # Способы оплаты #

    class Meta:
        model = Payment
        fields = ("__all__")

class WeightSerializer(serializers.ModelSerializer):
    # Вес #

    class Meta:
        model = Weight
        fields = ("__all__")
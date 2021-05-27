from rest_framework import fields, serializers

from .models import Contacts, Shedule, Payment, Delivery, Weight


class ContactsSerializer(serializers.ModelSerializer):
    # Контакты #

    class Meta:
        model = Contacts
        fields = ("__all__")
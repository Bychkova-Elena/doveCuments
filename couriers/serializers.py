from rest_framework import fields, serializers
from .models import Applications


class ApplicationsSerializer(serializers.ModelSerializer):
    # Заявки #

    class Meta:
        model = Applications
        fields = ("__all__")
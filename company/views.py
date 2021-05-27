from django.shortcuts import render

from .models import Contacts, Shedule, Payment, Delivery, Weight
from .serializers import ContactsSerializer

from rest_framework.response import Response
from rest_framework.views import APIView

class ContactsList(APIView):
  
    def get(self, request):
        '''Список контактов'''

        сontacts = Contacts.objects.all()
        serializer = ContactsSerializer(сontacts, many=True)
        return Response(serializer.data)

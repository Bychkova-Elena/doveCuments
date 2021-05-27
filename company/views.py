from django.shortcuts import render

from .models import Contacts, Shedule, Payment, Delivery, Weight
from .serializers import ContactsSerializer, DeliverySerializer, PaymentSerializer

from rest_framework.response import Response
from rest_framework.views import APIView

class ContactsList(APIView):
  
    def get(self, request):
        '''Список контактов'''

        сontacts = Contacts.objects.all()
        serializer = ContactsSerializer(сontacts, many=True)
        return Response(serializer.data)

class DeliveryList(APIView):
  
    def get(self, request):
        '''Список видов доставки'''

        delivery = Delivery.objects.all()
        serializer = DeliverySerializer(delivery, many=True)
        return Response(serializer.data)

class PaymentList(APIView):
  
    def get(self, request):
        '''Список способов оплаты'''

        payment = Payment.objects.all()
        serializer = PaymentSerializer(payment, many=True)
        return Response(serializer.data)

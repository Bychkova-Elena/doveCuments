import stripe

from django.conf import settings
from users.models import User
from django.http import Http404
from django.shortcuts import render

from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Order
from .serializers import OrdersSerializer

class CreateOrdersView(APIView):
  
    def post(self, request):
      order = OrdersSerializer(data=request.data)
      if order.is_valid():
          order.save()
          return Response(order.data, status=status.HTTP_201_CREATED)
      return Response(order.errors, status=status.HTTP_400_BAD_REQUEST)

class OrdersList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        orders = Order.objects.filter(user=request.user)
        serializer = OrdersSerializer(orders, many=True)
        return Response(serializer.data)



from django.shortcuts import render

from .models import Order
from .serializers import OrdersSerializer

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from django.http import Http404

class OrdersView(APIView):

    # def get(self, request):
    #   '''Список заказов'''

    #   orders = Order.objects.all()
    #   serializer = OrdersSerializer(orders, many=True)
    #   return Response(serializer.data)

    def post(self, request):
      order = OrdersSerializer(data=request.data)
      if order.is_valid():
          order.save()
          return Response(order.data, status=status.HTTP_201_CREATED)
      return Response(order.errors, status=status.HTTP_400_BAD_REQUEST)


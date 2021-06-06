import stripe

from django.conf import settings
from users.models import User
from django.http import Http404
from django.shortcuts import render

from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Applications
from .serializers import ApplicationsSerializer

class CreateApplicationsView(APIView):
  
    def post(self, request):
      app = ApplicationsSerializer(data=request.data)
      if app.is_valid():
          app.save()
          return Response(app.data, status=status.HTTP_201_CREATED)
      return Response(app.errors, status=status.HTTP_400_BAD_REQUEST)

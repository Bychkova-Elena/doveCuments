from django.urls import path, include

from company import views

urlpatterns = [
  path('contacts/', views.ContactsList.as_view()),
]
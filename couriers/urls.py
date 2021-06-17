from django.urls import path, include

from couriers import views

urlpatterns = [
    path('create-app/', views.CreateApplicationsView.as_view()),
]
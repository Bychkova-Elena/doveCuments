from django.urls import path, include

from orders import views

urlpatterns = [
  path('orders/', views.OrdersView.as_view()),
]
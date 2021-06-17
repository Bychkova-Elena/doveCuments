from django.urls import path, include

from orders import views

urlpatterns = [
    path('create-orders/', views.CreateOrdersView.as_view()),
    path('orders/', views.OrdersList.as_view()),
]
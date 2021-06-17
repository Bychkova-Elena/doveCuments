from django.urls import path, include

from company import views

urlpatterns = [
  path('contacts/', views.ContactsList.as_view()),
  path('delivery/', views.DeliveryList.as_view()),
  path('payment/', views.PaymentList.as_view()),
  path('weight/', views.WeightList.as_view()),
]
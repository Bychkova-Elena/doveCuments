from django.urls import path, include

from users import views

urlpatterns = [
    path('tokens/', views.TokensView.as_view()),
]
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/', include("company.urls")),
    # path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
]

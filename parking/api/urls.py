from django.urls import path
from api.views import *
from api import views

urlpatterns = [
    path('users/', views.user),
]
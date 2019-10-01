from django.urls import path, include
from . import views

urlpatterns = [
    path('userlist/', views.userlist)
]
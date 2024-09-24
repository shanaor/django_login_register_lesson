
from django.contrib import admin
from django.urls import path,include

from base import views

urlpatterns = [
    path('pri', views.test_pri), # private test
    path('pub', views.test_pub), # public test
    path('register', views.register),
    path('login', views.MyTokenObtainPairView.as_view()),
]

from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('generate_qr/', views.generate_qr, name="generate_qr"),
]
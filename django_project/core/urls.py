from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacto/', views.contacto, name='contacto'),
    path('acerca/', views.acerca, name='acerca'),
    path('servicios/', views.servicios, name='servicios'),
]

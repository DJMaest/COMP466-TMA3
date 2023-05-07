from django.urls import path
from . import views
urlpatterns=[
    path('', views.index, name="index-part3"),
    path('laptop/', views.laptop, name="laptop-part3"),
    path('laptop/<str:pk>/', views.laptopConfig, name="laptopConfig-part3"),
    path('bag/', views.bag, name="bag-part3"),
    path('order/', views.order, name="order-part3"),
    path('desktop/', views.desktop, name="desktop-part3"),
    path('desktop/<str:pk>/', views.desktopConfig, name="desktopConfig-part3"),
    path('contact/', views.contact, name="contact-part3"),
    path('search/', views.search, name="search-part3"),
    path('feedback/', views.feedback, name="feedback"),
]
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('profile/', views.profilePage, name="profile"),
    path('', views.index, name="index"),
    path('laptop/', views.laptop, name="laptop"),
    path('laptop/<str:pk>/', views.laptopConfig, name="laptopConfig"),
    path('bag/', views.bag, name="bag"),
    path('order/', views.order, name="order"),
    path('order-message/', views.orderMsg, name="order"),
    path('order-history/', views.orderHistory, name="orderHistory"),
    path('delete-order/<str:pk>', views.deleteOrder, name="deleteOrder"),
    path('order/<str:pk>/', views.orderDetails, name="orderDetails"),
    path('desktop/', views.desktop, name="desktop"),
    path('desktop/<str:pk>/', views.desktopConfig, name="desktopConfig"),
    path('contact/', views.contact, name="contact"),
    path('search/', views.search, name="search"),
    path('feedback/', views.feedback, name="feedback"),
    path('delete/', views.delete, name="delete"),
    path('password-reset/', views.ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/', 
    auth_views.PasswordResetConfirmView.as_view(template_name='part4/password_reset_confirm.html'),
    name='password_reset_confirm'),
    path('password-reset-complete/',
    auth_views.PasswordResetCompleteView.as_view(template_name='part4/password_reset_complete.html'),
    name='password_reset_complete'),

]
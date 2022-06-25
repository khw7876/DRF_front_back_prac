from django.contrib import admin
from django.urls import path, include
from user import views
urlpatterns = [
    path('', views.UserView.as_view()),
    path('sign_in/', views.LoginView.as_view()),
    path('sign_up/', views.UserView.as_view()),
]
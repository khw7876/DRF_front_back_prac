from django.contrib import admin
from django.urls import path, include
from post import views

urlpatterns = [
    path('', views.PostView.as_view()),
    # path('post/', views.PostView.as_view()),
    path('<int:post_id>/', views.PostView.as_view()),
]
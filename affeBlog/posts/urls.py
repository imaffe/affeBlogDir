from django.contrib import admin
from django.urls import  path

from posts import views
urlpatterns = [
    path('admin/', views.post_home),
]
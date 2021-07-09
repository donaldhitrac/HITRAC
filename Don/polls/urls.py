from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='polls-index'),
    path('home/', views.home, name='polls-home'),
]

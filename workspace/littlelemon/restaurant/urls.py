from django.urls import path
from . import views

app_name = 'restaurant'

urlpatterns = [
    path('', views.restaurant_view, name='index'),
]

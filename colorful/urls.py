from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('color/', views.colorize, name='colorize'),
]
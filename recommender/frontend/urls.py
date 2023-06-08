from django.urls import path
from . import views

urlpatterns = [
    path('', views.splash, name='splash'),
    path('home', views.home, name='home'),
    path('next', views.next, name='next')
]
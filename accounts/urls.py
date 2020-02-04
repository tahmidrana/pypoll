from django.urls import path, include
from . import views

urlpatterns = [
    path('login', views.login, name='accounts.login'),
    path('signup', views.signup, name='accounts.signup'),
]

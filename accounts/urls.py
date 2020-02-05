from django.urls import path, include
from . import views

urlpatterns = [
    path('login', views.LoginView.as_view(), name='accounts.login'),
    path('signup', views.signup_view, name='accounts.signup'),
    path('logout', views.logout_view, name='accounts.logout'),
]

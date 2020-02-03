from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='poll.home'),
    path('polls/<int:id>', views.view_poll, name='view_poll'),
    path('polls/new', views.new_poll, name='poll.new'),
]

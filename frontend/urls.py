from django.urls import path
from .views import *

app_name = 'frontend'

urlpatterns = [
    path('',Homepage, name='todo-list'),
]
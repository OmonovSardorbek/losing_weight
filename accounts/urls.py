from django.urls import path
from .views import *

urlpatterns = [
    path('create', create_user, name='create-user'),
    path('login', login, name='login'),
    path('logout/', logout, name='logout')
]

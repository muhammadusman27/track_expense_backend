from django.urls import path
from user_management.views import *


urlpatterns = [
    path('login', login, name='login'),
    path('signup', signup, name='signup')
]
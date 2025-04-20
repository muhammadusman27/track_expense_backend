from django.urls import path
from account.views import *

urlpatterns = [
    path('add', add, name='add'),
    path('list_account', list_account, name='list_account'),
    path('update', update, name='update'),
    path('delete', delete, name='delete'),
]

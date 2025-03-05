from django.urls import path
from item.views import *

urlpatterns = [
    path('add', add, name='add'),
    path('list_items', list_items, name='list_items'),
    path('update', update, name='update'),
    path('delete', delete, name='delete'),
]
from django.urls import path
from category.views import *

urlpatterns = [
    path('add', add, name='add'),
    path('list_categories', list_categories, name='list_categories'),
    path('update', update, name='update'),
    path('delete', delete, name='delete'),
]
from django.urls import path
from expense.views import *

urlpatterns = [
    path('add', add, name='add'),
    path('list_expenses', list_expenses, name='list_expenses'),
    path('chart', chart, name='chart'),
    path('update', update, name='update'),
    path('delete', delete, name='delete'),
]
from django.urls import path
from income.views import *

urlpatterns = [
    path('get_list_income', get_list_income, name='get_list_income'),
    path('add', create, name='create'),
    path('update', update, name='update'),
    path('delete', delete, name='delete'),

    # create income account crud
    path('create_income_amount', create_income_amount, name='create_income_amount'),
]
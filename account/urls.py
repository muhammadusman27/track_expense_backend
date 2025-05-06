from django.urls import path
from account.views import *

urlpatterns = [
    path('add', add, name='add'),
    path('list_account', list_account, name='list_account'),
    path('update', update, name='update'),
    path('delete', delete, name='delete'),

    # view all transections history
    path('list_all_transaction', list_all_transaction, name='list_all_transaction'),
]

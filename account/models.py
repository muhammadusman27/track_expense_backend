from django.db import models
from django_userforeignkey.models.fields import UserForeignKey

# Create your models here.


class Account(models.Model):
    name = models.CharField(max_length=150, db_column='name')
    balance = models.FloatField(default=0, db_column='balance')
    created_at = models.DateTimeField(auto_now_add=True, db_column='created_at')
    user = UserForeignKey(auto_user_add=True, null=True, blank=True, on_delete=models.SET_NULL, db_column='user')

    class Meta:
        ordering = ['-id']
        db_table = 'Account'


class Transaction(models.Model):
    account = models.ForeignKey(to='account.Account', null=True, blank=True, on_delete=models.SET_NULL, db_column='account')
    transaction_type = models.CharField(max_length=7, choices=[("CREDIT", "CREDIT"), ("DEBIT", "DEBIT")], null=False, db_column="transaction_type")
    expense = models.ForeignKey(to='expense.Expense', null=True, blank=True, on_delete=models.SET_NULL, db_column='expense')
    income_amount = models.ForeignKey(to='income.IncomeAmount', null=True, blank=True, on_delete=models.SET_NULL, db_column='income_amount')

    created_at = models.DateTimeField(auto_now_add=True, db_column='created_at')
    user = UserForeignKey(auto_user_add=True, null=True, blank=True, on_delete=models.SET_NULL, db_column='user')

    class Meta:
        ordering = ['id']
        db_table = 'Transaction'
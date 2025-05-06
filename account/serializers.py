from rest_framework import serializers
from account.models import Account, Transaction

class AccountSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Account
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    account_name = serializers.CharField(source='account.name', allow_null=True, allow_blank=True, required=False)
    expense_name = serializers.CharField(source='expense.name', allow_null=True, allow_blank=True, required=False)
    expense_amount = serializers.FloatField(source='expense.price', allow_null=True, required=False)
    expense_category = serializers.CharField(source='expense.category.name', allow_null=True, allow_blank=True, required=False)

    class Meta:
        model = Transaction
        fields = [field.name for field in Transaction._meta.get_fields()] + ['account_name', 'expense_name', 'expense_amount', 'expense_category']
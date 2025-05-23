from rest_framework import serializers
from expense.models import Expense

class ExpenseSerializer(serializers.ModelSerializer):
    item_name = serializers.CharField(source='item.name', allow_null=True, allow_blank=True, required=False)
    category_name = serializers.CharField(source='category.name', allow_null=True, allow_blank=True, required=False)
    account_name = serializers.CharField(source="account.name", required=False, allow_null=True, read_only=True)
    
    class Meta:
        model = Expense
        fields = '__all__'
        ['item','category', 'quantity', 'name', 'description', 'price', 'weight', 'weight_unit', 'date', 'item_name',
         'category_id', 'category_name', 'user', 'account_name']
        
        
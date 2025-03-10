from rest_framework import serializers
from expense.models import Expense

class ExpenseSerializer(serializers.ModelSerializer):
    item_name = serializers.CharField(source='item.name', allow_null=True, allow_blank=True, required=False)
    category_id = serializers.CharField(source='item.category.id', allow_null=True, allow_blank=True, required=False)
    category_name = serializers.CharField(source='item.category.name', allow_null=True, allow_blank=True, required=False)
    
    class Meta:
        model = Expense
        fields = '__all__'
        ['item', 'quantity', 'description', 'price', 'weight', 'weight_unit', 'date', 'item_name',
         'category_id', 'category_name']
        
        
from rest_framework import serializers
from item.models import Item

class ItemSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', allow_null=True, allow_blank=True, required=False)

    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'category', 'category_name']


from income.models import Income, IncomeAmount
from rest_framework import serializers


class IncomeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Income
        fields = '__all__'


class IncomeAmountSerializer(serializers.ModelSerializer):

    class Meta:
        model = IncomeAmount
        fields = '__all__'
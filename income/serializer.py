from income.models import Income, IncomeAmount
from account.models import Account
from rest_framework import serializers


class IncomeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Income
        fields = '__all__'


class IncomeAmountSerializer(serializers.ModelSerializer):

    class Meta:
        model = IncomeAmount
        fields = '__all__'
    

    def create(self, validated_data):
        amount = int(validated_data['amount'])
        income = validated_data['income']
        account = validated_data['account']
        request = self.context.get('request')
        user = request.user if request else None
        if user:
            user_id = user.id
            if amount:
                try:
                    amount = float(amount)
                    if amount < 0:
                        raise serializers.ValidationError({
                            'amount': 'This value must be greater than 0.'
                        })
                except Exception as ex_amount:
                    raise serializers.ValidationError({
                        'amount': 'This value must be greater than 0.'
                    })
            if income:
                try:
                    Income.objects.get(user_id=user_id, id=income.id)
                except Exception as ex_income:
                    print(ex_income)
                    raise serializers.ValidationError({"income": "Invalid income value."})
            if account:
                try:
                    Account.objects.get(user_id=user_id, id=account.id)
                except Exception as ex_account:
                    raise serializers.ValidationError({"amount": "Invalid account value."})
            return super().create(validated_data)
        else:
            raise serializers.ValidationError({'user': "Invalid user"})
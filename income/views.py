from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from income.serializer import IncomeSerializer, IncomeAmountSerializer
from income.models import Income, IncomeAmount
from account.models import Account

# Create your views here.

@permission_classes([IsAuthenticated])
@api_view(['GET'])
def get_list_income(request):
    incomes = Income.objects.filter(user_id=request.user.id)
    serializer = IncomeSerializer(incomes, many=True)
    return Response(data={"data": serializer.data})


@permission_classes([IsAuthenticated])
@api_view(['POST'])
def create(request):
    data = request.data
    serializer = IncomeSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={"data": serializer.data})
    return Response(data={"data": {}, "errors": serializer.errors})


@permission_classes([IsAuthenticated])
@api_view(['POST'])
def update(request):
    income_id = request.GET.get('income_id', None)
    income_obj = Income.objects.get(id=int(income_id), user_id=request.user.id)
    data = request.data
    serializer = IncomeSerializer(income_obj, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={"data": serializer.data, "message": "Income Updated!", "errors": ""})
    else:
        return Response(data={"data": {}, "message": "Income did't updated!", "errors": serializer.errors})


@permission_classes([IsAuthenticated])
@api_view(['DELETE'])
def delete(request):
    income_id = request.GET.get('income_id', None)
    try:
        Income.objects.filter(id=int(income_id)).delete()
    except Exception as e:
        return Response(data={"data": {}, "message": "Income Delted!", "errors": ""})
    return Response(data={"data": {}, "message": "Income Delted!", "errors": ""})


@permission_classes([IsAuthenticated])
@api_view(['POST'])
def create_income_amount(request):
    data = request.data
    serializer = IncomeAmountSerializer(data=data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        obj = IncomeAmount.objects.get(id=serializer.data['id'])
        if obj:
            account_obj = Account.objects.get(user_id=request.user.id, id=obj.account.id)
            account_obj.balance = account_obj.balance + obj.amount
            account_obj.save()
        return Response(data={"data": serializer.data})
    return Response(data={"data": {}, "errors": serializer.errors})


@permission_classes([IsAuthenticated])
@api_view(['GET'])
def list_income_amount(request):
    incomes = IncomeAmount.objects.filter(user_id=request.user.id)
    serializer = IncomeAmountSerializer(incomes, many=True)
    return Response(data={"data": serializer.data})
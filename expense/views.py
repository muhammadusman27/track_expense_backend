from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from expense.serializers import ExpenseSerializer
from rest_framework.permissions import IsAuthenticated
from expense.models import Expense
from django.db.models import Sum
from account.models import Transaction, Account


# Create your views here.


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add(request):
    data = request.data
    serializer = ExpenseSerializer(data=data)
    if serializer.is_valid():
        try:
            account_id = serializer.validated_data['account']
            account_obj = Account.objects.get(id=account_id.id, user_id=request.user.id)
            if account_obj.balance > serializer.validated_data['price']:
                serializer.save()
                Transaction.objects.create(
                    account_id=serializer.data['account'],
                    transaction_type="DEBIT",
                    expense_id=serializer.data['id'],
                    income_amount=None
                )
                account_obj.balance = account_obj.balance - serializer.data['price']
                account_obj.save()
                return Response(data={"data": serializer.data, "message": "Expense created successfully."})
        except Exception as ex:
            return Response(data={"data": {}, "message": f"Issue in Account balance or {ex}"})
        
    return Response(data={"data": {}, "message": serializer.errors})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_expenses(request):
    category_id = request.GET.get('category_id', None)
    expenses = Expense.objects.filter(user_id=request.user.id)
    if category_id:
        expenses = expenses.filter(category_id=category_id)
    serializer = ExpenseSerializer(expenses, many=True)
    return Response(data={"data": serializer.data, "message": "all data"})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def chart(request):
    expenses = Expense.objects.values('category__name').annotate(total=Sum('price'))
    labels = [x['category__name'] for x in expenses]
    data = [x['total'] for x in expenses]
    print(f"labels = ", labels)
    print(f"data = ", data)
    return Response(data={
        "data": 
        {
            "labels": labels,
            "data": data
        },

        "message": "all data"
    })


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update(request):
    expense_id = request.GET.get('expense_id')
    data = request.data
    try:
        expense = Expense.objects.get(id=int(expense_id), user_id=request.user.id)
        serializer = ExpenseSerializer(expense, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"data": serializer.data, "message": "Expense updated successfully."})
        return Response(data={"data": {}, "message": serializer.errors})
    except Exception as e:
        return Response(data={"data": {}, "message": f"{e}"})


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete(request):
    expense_id = request.GET.get('expense_id')
    try:
        expense = Expense.objects.filter(id=int(expense_id), user_id=request.user.id).delete()
        return Response(data={"data": {}, "message": "Expense deleted successfully."})
    except Exception as e:
        return Response(data={"data": {}, "message": f"{e}"})
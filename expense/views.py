from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from expense.serializers import ExpenseSerializer
from rest_framework.permissions import IsAuthenticated
from expense.models import Expense


# Create your views here.


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add(request):
    data = request.data
    serializer = ExpenseSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={"data": serializer.data, "message": "Expense created successfully."})
    return Response(data={"data": {}, "message": serializer.errors})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_expenses(request):
    expenses = Expense.objects.all()
    serializer = ExpenseSerializer(expenses, many=True)
    return Response(data={"data": serializer.data, "message": "all data"})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update(request):
    expense_id = request.GET.get('expense_id')
    data = request.data
    try:
        expense = Expense.objects.get(id=int(expense_id))
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
        expense = Expense.objects.filter(id=int(expense_id)).delete()
        return Response(data={"data": {}, "message": "Expense deleted successfully."})
    except Exception as e:
        return Response(data={"data": {}, "message": f"{e}"})
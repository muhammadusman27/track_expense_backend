from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from account.serializers import AccountSerializer, TransactionSerializer
from account.models import Account, Transaction
from rest_framework.permissions import IsAuthenticated



# Create your views here.


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add(request):
    data = request.data
    serializer = AccountSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={"data": serializer.data, "message": "Account created successfully."})
    return Response(data={"data": {}, "message": serializer.errors})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_account(request):
    categories = Account.objects.filter(user_id=request.user.id)
    serializer = AccountSerializer(categories, many=True)
    return Response(data={"data": serializer.data, "message": "all data"})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update(request):
    account_id = request.GET.get('account_id')
    data = request.data
    try:
        category = Account.objects.get(id=int(account_id), user_id=request.user.id)
        serializer = AccountSerializer(category, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"data": serializer.data, "message": "Account updated successfully."})
        return Response(data={"data": {}, "message": serializer.errors})
    except Exception as e:
        return Response(data={"data": {}, "message": f"{e}"})


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete(request):
    account_id = request.GET.get('account_id')
    try:
        account = Account.objects.filter(id=int(account_id), user_id=request.user.id).delete()
        return Response(data={"data": {}, "message": "Account deleted successfully."})
    except Exception as e:
        return Response(data={"data": {}, "message": f"{e}"})
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_all_transaction(request):
    user_id = request.user.id
    all_transaction = Transaction.objects.filter(user_id=user_id).order_by('-id')
    serializer = TransactionSerializer(all_transaction, many=True)
    return Response(data={"data": serializer.data, "message": "all data"})

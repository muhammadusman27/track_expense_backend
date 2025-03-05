from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from item.serializers import ItemSerializer
from item.models import Item

# Create your views here.

@api_view(['POST'])
def add(request):
    data = request.data
    serializer = ItemSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={"data": serializer.data, "message": "Item created successfully."})
    return Response(data={"data": {}, "message": serializer.errors})


@api_view(['GET'])
def list_items(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(data={"data": serializer.data, "message": "all data"})


@api_view(['POST'])
def update(request):
    item_id = request.GET.get('item_id')
    data = request.data
    print(f"data = {data}")
    try:
        item = Item.objects.get(id=int(item_id))
        serializer = ItemSerializer(item, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"data": serializer.data, "message": "Item updated successfully."})
        return Response(data={"data": {}, "message": serializer.errors})
    except Exception as e:
        return Response(data={"data": {}, "message": f"{e}"})


@api_view(['DELETE'])
def delete(request):
    item_id = request.GET.get('item_id')
    try:
        item = Item.objects.filter(id=int(item_id)).delete()
        return Response(data={"data": {}, "message": "Item deleted successfully."})
    except Exception as e:
        return Response(data={"data": {}, "message": f"{e}"})
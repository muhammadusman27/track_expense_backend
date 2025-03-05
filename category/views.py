from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from category.serializers import CategorySerializer
from category.models import Category


# Create your views here.


@api_view(['POST'])
def add(request):
    data = request.data
    serializer = CategorySerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={"data": serializer.data, "message": "Category created successfully."})
    return Response(data={"data": {}, "message": serializer.errors})


@api_view(['GET'])
def list_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(data={"data": serializer.data, "message": "all data"})


@api_view(['POST'])
def update(request):
    category_id = request.GET.get('category_id')
    data = request.data
    try:
        category = Category.objects.get(id=int(category_id))
        serializer = CategorySerializer(category, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"data": serializer.data, "message": "Category updated successfully."})
        return Response(data={"data": {}, "message": serializer.errors})
    except Exception as e:
        return Response(data={"data": {}, "message": f"{e}"})


@api_view(['DELETE'])
def delete(request):
    category_id = request.GET.get('category_id')
    try:
        category = Category.objects.filter(id=int(category_id)).delete()
        return Response(data={"data": {}, "message": "Category deleted successfully."})
    except Exception as e:
        return Response(data={"data": {}, "message": f"{e}"})
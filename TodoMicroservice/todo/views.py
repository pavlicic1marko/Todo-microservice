from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .todos import products
from todo.models import Todo
from todo.serializer import TodoSerializer




# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getRoutes(request):
    routes = ['api/products', 'api/products/<id>']
    return Response(routes)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProducts(request):

    todo = Todo.objects.all()
    serializer = TodoSerializer(todo, many=True)

    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def getProductsById(request, pk):
    product = None
    for i in products:
        if i['_id'] == pk:
            product = i
            break


    return Response(product)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createTodo(request):
    data = request.data
    pass
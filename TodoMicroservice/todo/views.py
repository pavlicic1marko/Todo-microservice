from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from todo.models import Todo
from todo.serializer import TodoSerializer
import django.core.exceptions



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

    todo = Todo.objects.get(_id=pk)
    serializer = TodoSerializer(todo, many=False)


    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createTodo(request):
    data = request.data
    pass

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delTodo(request, pk):
    todo_id = pk

    try:
        todo = Todo.objects.get(_id=todo_id)
        todo.delete()
        return Response('todo is deleted', status=200)

    except django.core.exceptions.ObjectDoesNotExist:

        return Response('todo with id:'+ todo_id+ ', does not exist', status=status.HTTP_404_NOT_FOUND)
    except Exception as e:

        return Response(e, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from todo.models import Todo
from todo.serializer import TodoSerializer
import django.core.exceptions
import jwt
from django.conf import settings


# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getRoutes(request):
    routes = ['api/products', 'api/products/<id>']
    return Response(routes)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getTodoByUserId(request):

    bearer_token = request.headers['Authorization'].split()[1]
    payload = jwt.decode(jwt=bearer_token, key=settings.SIMPLE_JWT['SIGNING_KEY'], algorithms=['HS256'])
    use_id = payload['user_id']


    todo = Todo.objects.filter(user_id=use_id)
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

    bearer_token = request.headers['Authorization'].split()[1]
    payload = jwt.decode(jwt=bearer_token, key=settings.SIMPLE_JWT['SIGNING_KEY'], algorithms=['HS256'])
    use_id = payload['user_id']

    todo = Todo.objects.create(
        user_id=use_id,
        title = data['title'],
        description = data['description']
        )
    serializer = TodoSerializer(todo, many=False)
    return Response(serializer.data)


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
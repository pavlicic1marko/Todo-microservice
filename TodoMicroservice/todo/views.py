from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


# Create your views here.

@api_view(['GET'])
@permission_classes([AllowAny])
def getRoutes(request):
    routes = ['api/products', 'api/products/<id>']
    return Response(routes)

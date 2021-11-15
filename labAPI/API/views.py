from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from rest_framework.authtoken.models import Token



from django.db.models.signals import post_save

from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
def sign_up(request):
    serializer = userSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        account = serializer.save()
        data['response'] = 'successfully registered new user.'
        data['email'] = account.email
        data['username'] = account.username
        # data['token'] = Token.objects.get(user=userSerializer).key
    else:
        data = serializer.errors
    return Response(data)
# def sign_up(request):
#     data = {'data':'','status':''}
#     serializer = userSerializer(data=request.data)
#     if serializer.is_valid():
#         print('noha')
#     serializer.save()
#         # data['data'] = userSerializer.get_value('')
#     return Response(data=serializer.data)


@api_view(['GET'])
def hello(request):
    data = {'message' :'he'}
    return Response(data=data)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])

def movie_list(request):
    movies = movie.objects.all()
    serializer = movieSerializer(instance=movies,many=True)
    return Response(data=serializer.data)


@api_view(['POST'])
def create_movie(request):

    serializer = movieSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(data=serializer.data)



@api_view(['GET'])
def detail_movie(requset,pk):

    movies = movie.objects.get(pk=pk)
    serializer = movieSerializer(instance=movies)
    return Response(data=serializer.data)

@api_view(['DELETE'])
def delete_movie(requset,pk):

    movies = movie.objects.get(pk=pk)
    movies.delete()
    return Response({'Deleted successfully'})

@api_view(['PUT'])
def put(request, pk):

    movies = movie.objects.get(pk=pk)
    serializer = movieSerializer(instance=movies,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)


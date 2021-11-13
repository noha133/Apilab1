from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *





@api_view(['GET'])
def hello(request):
    data = {'message' :'he'}
    return Response(data=data)

@api_view(['GET'])
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


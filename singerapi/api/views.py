from rest_framework.response import Response
from rest_framework import pagination, status
# from rest_framework.decorators import api_view, permission_classes, authentication_classes,throttle_classes
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework import generics

from django_filters.rest_framework import DjangoFilterBackend
from singerapi.models import Singer, SongList
from singerapi.api.permissions import AdminOrReadOnly
from singerapi.api.serializers import SingerSerializer, SongListSerializer
from singerapi.api.pagination import SongListPagination,SingerListPagination

# class Based Views

class SingerListGV(generics.ListAPIView):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['singer_name','id']
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['singer_name','id']
    # filter_backends = [filters.OrderingFilter]
    pagination_class = SingerListPagination


class SingerListAV(APIView):
    # throttle_classes = [UserRateThrottle,AnonRateThrottle]
    # permission_classes = [IsAuthenticated]
    # permission_classes = [AdminOrReadOnly]
    # authentication_classes = [BasicAuthentication]
    def get(self, request):
        singers = Singer.objects.all()
        serializer = SingerSerializer(singers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SingerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class SingerDetails(APIView):
    # throttle_classes = [UserRateThrottle,AnonRateThrottle]
    # permission_classes = [IsAuthenticated]
    # permission_classes = [AdminOrReadOnly]
    def get(self, request, pk):
        try:  
            singer = Singer.objects.get(pk=pk)
        except Singer.DoesNotExist:
            return Response({'Error': 'Singer not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = SingerSerializer(singer)
        return Response(serializer.data)
    
    def put(self, request,pk):
        singer = Singer.objects.get(pk=pk)
        serializer = SingerSerializer(singer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request,pk):
        singer = Singer.objects.get(pk=pk)
        singer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SongListGV(generics.ListAPIView):
    queryset = SongList.objects.all()
    serializer_class = SongListSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['title','duration','singer','id']
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['title','duration']
    # filter_backends = [filters.OrderingFilter]
    pagination_class = SongListPagination

class SongListAV(APIView):
    # throttle_classes = [UserRateThrottle,AnonRateThrottle]
    # permission_classes = [IsAuthenticated]
    # permission_classes = [AdminOrReadOnly]
    # authentication_classes = [BasicAuthentication]
    def get(self, request):
        songs = SongList.objects.all()
        serializer = SongListSerializer(songs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SongListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class SongDetails(APIView):
    # throttle_classes = [UserRateThrottle,AnonRateThrottle]
    # permission_classes = [IsAuthenticated]
    # permission_classes = [AdminOrReadOnly]
    def get(self, request,pk):
        try:  
            song = SongList.objects.get(pk=pk)
        except SongList.DoesNotExist:
            return Response({'Error': 'Song not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = SongListSerializer(song)
        return Response(serializer.data)
    
    def put(self, request,pk):
        song = SongList.objects.get(pk=pk)
        serializer = SongListSerializer(song, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request,pk):
        song = SongList.objects.get(pk=pk)
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#Function Based Views

# @api_view(['GET', 'POST'])
# @throttle_classes([UserRateThrottle,AnonRateThrottle])
# # @authentication_classes([BasicAuthentication])
# # @permission_classes([IsAuthenticated])
# def singer_list(request):
#     if request.method == 'GET':
#         singers = Singer.objects.all()
#         serializer = SingerSerializer(singers, many=True)
#         return Response(serializer.data)
    
#     if request.method == 'POST':
#         serializer = SingerSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

# @api_view(['GET', 'PUT', 'DELETE'])
# @throttle_classes([UserRateThrottle,AnonRateThrottle])
# @permission_classes([IsAuthenticated])
# def singer_details(request, pk):
#     if request.method == 'GET':  
#         try:  
#             singer = Singer.objects.get(pk=pk)
#         except Singer.DoesNotExist:
#             return Response({'Error': 'Singer not found'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = SingerSerializer(singer)
#         return Response(serializer.data)
    
#     if request.method == 'PUT':
#         singer = Singer.objects.get(pk=pk)
#         serializer = SingerSerializer(singer, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     if request.method == 'DELETE':
#         singer = SongList.objects.get(pk=pk)
#         singer.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET', 'POST'])
# @throttle_classes([UserRateThrottle,AnonRateThrottle])
# # @authentication_classes([BasicAuthentication])
# # @permission_classes([IsAuthenticated])
# def song_list(request):
#     if request.method == 'GET':
#         songs = SongList.objects.all()
#         serializer = SongListSerializer(songs, many=True)
#         return Response(serializer.data)
    
#     if request.method == 'POST':
#         serializer = SongListSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

# @api_view(['GET', 'PUT', 'DELETE'])
# @throttle_classes([UserRateThrottle,AnonRateThrottle])
# @permission_classes([IsAuthenticated])
# def song_details(request, pk):
#     if request.method == 'GET':  
#         try:  
#             song = SongList.objects.get(pk=pk)
#         except SongList.DoesNotExist:
#             return Response({'Error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = SongListSerializer(song)
#         return Response(serializer.data)
    
#     if request.method == 'PUT':
#         song = SongList.objects.get(pk=pk)
#         serializer = SongListSerializer(song, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     if request.method == 'DELETE':
#         song = SongList.objects.get(pk=pk)
#         song.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
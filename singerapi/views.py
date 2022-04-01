# from rest_framework import viewsets
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
# from singerapi.models import Singer, SongList
# from singerapi.api.serializers import SingerSerializer, SongListSerializer
# from singerapi.api.pagination import SongListPagination,SingerListPagination


# class SingerViewSet(viewsets.ModelViewSet):
#     queryset = Singer.objects.all()
#     serializer_class = SingerSerializer
#     pagination_class = SingerListPagination
#     throttle_classes = [UserRateThrottle,AnonRateThrottle]
#     permission_classes = [IsAuthenticated]
    
# class SongViewSet(viewsets.ModelViewSet):
#     queryset = SongList.objects.all()
#     serializer_class = SongListSerializer
#     pagination_class = SongListPagination
#     throttle_classes = [UserRateThrottle,AnonRateThrottle]
#     permission_classes = [IsAuthenticated]



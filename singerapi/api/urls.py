from django.urls import path
from singerapi.api.views import SingerListAV,SingerListGV,SingerDetails,SongListAV,SongListGV,SongDetails #Singer_list,song_list,singer_details,song_details


urlpatterns = [

    # path('singer/', singer_list, name='singer-list'),
    # path('singer/<int:pk>/', singer_details, name='singer-details'),
    # path('song/', song_list, name='song-list'),
    # path('song/<int:pk>/', song_details, name='song-details'),

    path('singerlist/', SingerListGV.as_view(), name='singer-list'),
    path('singer/', SingerListAV.as_view(), name='singer-list'),
    path('singer/<int:pk>/', SingerDetails.as_view(), name='singer-details'),

    path('songlist/', SongListGV.as_view(), name='song-list'),
    path('song/', SongListAV.as_view(), name='song-list'),
    path('song/<int:pk>/', SongDetails.as_view(), name='song-details'),
]
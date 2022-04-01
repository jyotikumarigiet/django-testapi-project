from django.forms import ValidationError
from rest_framework import serializers
from singerapi.models import Singer, SongList

class SongListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SongList
        #  fields = ['title',]
        fields = "__all__"

    def validate(self, data):
        if data['title']:
            for n in data['title']:
                if n.isdigit():
                    raise serializers.ValidationError({'error' : "Title cannot be numeric!"})
                return data

class SingerSerializer(serializers.ModelSerializer):
    song_list = SongListSerializer(many=True, read_only=True)                               #(many to one/one to many all song_list with one singer)
    class Meta:
        model = Singer
        fields = "__all__"
    
    def validate(self, data):
        if data['singer_name']:
            for n in data['singer_name']:
                if n.isdigit():
                    raise serializers.ValidationError({'error' : "Name cannot be numeric!"})
                return data























# class SongListSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=50)
#     duration = serializers.FloatField()

#     def create(self, validated_data):
#         return SongList.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.duration = validated_data.get('duration', instance.duration)
#         instance.save()
#         return instance

# class SingerSerializer(serializers.Serializer):
#     song_list = SongListSerializer(many=True, read_only=True)
#     id = serializers.IntegerField(read_only=True)
#     singer_name = serializers.CharField(max_length=30)
#     def create(self, validated_data):
#         return Singer.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.singer_name = validated_data.get('singer_name', instance.singer_name)
#         instance.save()
#         return instance
#     def validate(self, data):
#         if data['singer_name'] == data['singer_name']:
#             raise serializers.ValidationError("Name should be different!")
#         else:
#             return data
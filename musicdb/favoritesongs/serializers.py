from rest_framework import serializers
from favoritesongs.models import User, Song


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('id', 'title', 'artist', 'album')


class UserSerializer(serializers.ModelSerializer):
    favorite_songs = SongSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = ('id',  'name', 'email', 'favorite_songs')



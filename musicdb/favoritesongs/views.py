from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from django.shortcuts import render_to_response
from favoritesongs.models import User, Song
from favoritesongs.serializers import UserSerializer, SongSerializer


def index(request):
    return render_to_response('index.html')


class Users(APIView):
    """
    User api.
    """
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        user = User()
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Songs(APIView):
    """
    Songs api.
    """
    def get(self, request, format=None):
        users = Song.objects.all()
        serializer = SongSerializer(users, many=True)
        return Response(serializer.data)

    # Currently not in use
    # def post(self, request, format=None):
    #     song = Song()
    #     serializer = SongSerializer(song, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # def delete(self, request, pk, format=None):
    #     song = self.get_object(pk)
    #     song.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


class UserFavSongs(APIView):
    """
    UserFavSongs api.
    """
    def get(self, request, pk, format=None):
        user = User.objects.get(id=pk)
        fav_songs = user.favorite_songs.all()
        serializer = SongSerializer(fav_songs, many=True)
        return Response(serializer.data)

    def post(self, request, pk, format=None):

        user = User.objects.get(id=pk)
        song = Song.objects.get(id=request.data['song_id'])

        if request.data['command'] == 'add':
            user.favorite_songs.add(song)
            user.save()
            return Response(status=status.HTTP_200_OK)

        elif request.data['command'] == 'delete':
            user.favorite_songs.remove(song)
            return Response(status=status.HTTP_204_NO_CONTENT)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

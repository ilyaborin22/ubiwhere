from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class User(models.Model):
    email = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    favorite_songs = models.ManyToManyField(Song)

    def __str__(self):
        return self.name

from django.db import models


class User(models.Model):
    email = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name + ', ' + self.email


class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)

    def __str__(self):
        return 'title:' + self.title + ', artist: ' + self.artist + ', album: ' + self.album + '\n'


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)



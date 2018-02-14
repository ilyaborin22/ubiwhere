from django.core.management.base import BaseCommand
import requests
from favoritesongs.models import Song

class Command(BaseCommand):

    def _populate_songs(self):
        """Calls the public RESTApi to get the songs data and then inserts it into the local DB using the model"""
        response = requests.get('http://freemusicarchive.org/recent.json')
        assert response.status_code == 200

        # revrieve the song data from the JSON and insert it into the DB
        for track in response.json()['aTracks']:
            print(track)
            song = Song(title=track['track_title'],
                        artist=track['artist_name'],
                        album=track['album_title'])
            song.save()

    def handle(self, *args, **options):
        self._populate_songs()

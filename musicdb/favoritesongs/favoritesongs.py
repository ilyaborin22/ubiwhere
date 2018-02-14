# from django.views import generic
#
# app_name = "app"
#
# class FavoriteSongsApp():
#     template_name = 'templates/users.html'

from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from favoritesongs import views


user_api_patterns = [
    url(r'^api/users/$', views.Users.as_view()),
    url(r'^api/users/(?P<pk>[0-9]+)/$', views.Users.as_view()),
]

song_api_patterns = [
    url(r'^api/songs/$', views.Songs.as_view()),
    url(r'^api/songs/user/(?P<pk>[0-9]+)/$', views.UserFavSongs.as_view()),
]

urlpatterns = [
    url(r'^$', views.index),
    url(r'^users/$', views.index),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
              user_api_patterns + song_api_patterns

urlpatterns = format_suffix_patterns(urlpatterns)


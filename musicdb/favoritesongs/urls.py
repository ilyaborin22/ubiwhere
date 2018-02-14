from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from favoritesongs import views


urlpatterns = [
    url(r'^users/$', views.index),
    url(r'^users/api/$', views.Users.as_view()),
    url(r'^users/api/(?P<pk>[0-9]+)/$', views.Users.as_view()),
    # url(r'^app/users/user/(?P<pk>[0-9]+)/fav-songs/$', views.user_fav_songs),
    url(r'^songs/$', views.songs),
    url(r'^songs/api/$', views.Songs.as_view()),
    url(r'^songs/api/(?P<pk>[0-9]+)/$', views.Songs.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)


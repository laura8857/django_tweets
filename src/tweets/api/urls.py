from django.conf.urls import url
from django.views.generic.base import RedirectView

from .views import TweetListAPIView,TweetCreateAPIView,RetweetAPIView

urlpatterns = [
    # url(r'^$', RedirectView.as_view(url='/'),name="list"),
    url(r'^$', TweetListAPIView.as_view(),name="list"),
    url(r'^create/$', TweetCreateAPIView.as_view(), name="create"),
    url(r'^(?P<pk>\d+)/retweet/$', RetweetAPIView.as_view(),name="retweet"),
    # url(r'^(?P<pk>\d+)/update$', TweetUpdateView.as_view(),name="update"),
    # url(r'^(?P<pk>\d+)/delete$', TweetDeleteView.as_view(),name="delete"),
]

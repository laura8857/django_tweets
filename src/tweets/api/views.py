from rest_framework import generics
from django.db.models import Q
from rest_framework import permissions

from tweets.models import Tweet
from .serializers import TweetModelSerialzer
from .pagination import StandardResultPagination


class TweetCreateAPIView(generics.CreateAPIView):
    serializer_class = TweetModelSerialzer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TweetListAPIView(generics.ListAPIView):
    serializer_class = TweetModelSerialzer
    pagination_class = StandardResultPagination

    def get_queryset(self,*args,**kwargs):
        im_follow = self.request.user.profile.get_following()
        qs1 = Tweet.objects.filter(user__in=im_follow)
        qs2 = Tweet.objects.filter(user=self.request.user)
        qs = (qs1|qs2).distinct().order_by("-timestamp")
        # print(self.request.GET)
        query = self.request.GET.get("q",None)
        if query is not None:
            qs = qs.filter(
                Q(content__icontains = query) |
                Q(user__username__icontains = query)
                           )
        return qs
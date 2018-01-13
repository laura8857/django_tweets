from django.shortcuts import render,get_object_or_404
from django.views.generic import DetailView,ListView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy,reverse
from django.db.models import Q

from .models import Tweet
from .forms import TweetModelForm
from .mixins import FormUserNeededMixin,UserOwnerMixin
# Create your views here.


class TweetCreateView(LoginRequiredMixin,FormUserNeededMixin,CreateView):
    form_class = TweetModelForm
    template_name = "tweets/create_view.html"
    # success_url = "/tweet/"   #becasue there is get_absolute_url in models.py
    login_url = '/admin/'

class TweetUpdateView(LoginRequiredMixin,UserOwnerMixin,UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = "tweets/update_view.html"
    # success_url = "/tweet/" #becasue there is get_absolute_url in models.py

class TweetDeleteView(LoginRequiredMixin,DeleteView):
    model = Tweet
    template_name = "tweets/delete_confirm.html"
    success_url = reverse_lazy("tweet:list") # namespace:name



class TweetDetailView(DetailView):
    template_name = "tweets/detail_view.html"
    queryset = Tweet.objects.all()

    def get_object(self):
        # for check the pk of object
        # e.q. {'pk': '1'}
        # print(self.kwargs)
        pk = self.kwargs.get("pk")
        obj = get_object_or_404(Tweet,pk =pk)
        return obj
        # return Tweet.objects.get(id=pk)

class TweetListView(ListView):
    template_name = "tweets/list_view.html"
    queryset = Tweet.objects.all()

    def get_queryset(self,*args,**kwargs):
        qs = Tweet.objects.all()
        # print(self.request.GET)
        query = self.request.GET.get("q",None)
        if query is not None:
            qs = qs.filter(
                Q(content__icontains = query) |
                Q(user__username__icontains = query)
                           )
        return qs

    def get_context_data(self, *args,**kwargs):
        context = super(TweetListView,self).get_context_data(*args,**kwargs)
        context["create_form"] =  TweetModelForm()
        context["create_url"] = reverse_lazy("tweet:create")
        return context

# def tweet_detail_view(request ,id=1):
#     obj = Tweet.objects.get(id=id)
#     context = {
#         "object":obj
#     }
#     return render(request,"tweets/detail_view.html",context)
#
# def tweet_list_view(request ,id=1):
#     queryset = Tweet.objects.all()
#     context = {
#         "object_list":queryset
#     }
# #     return render(request,"tweets/list_view.html",context)
#
#
# def tweet_create_view(request):
#     form = TweetModelForm(request or None)
#
#     if form.is_valid():
#         instance = form.save(False)
#         instance.user = request.user
#
#         instance.save()
#     context = {
#         "form":form
#     }
#     return render(request,"tweets/create_view.html",context)

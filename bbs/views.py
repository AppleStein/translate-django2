#url https://noauto-nolife.com/post/startup-django/

from multiprocessing import context
from pydoc_data.topics import topics
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from .models import Topic

class IndexView(View):
    def get(self, request, *args, **kwargs):

        topics = Topic.objects.all()
        context={"topics":topics}

        return render(request, "bbs/index.html", context)

    def post(self, request, *args, **kwargs):
        posted = Topic(comment = request.POST["comment"])
        posted.save()

        return redirect("bbs:index")

index = IndexView.as_view()
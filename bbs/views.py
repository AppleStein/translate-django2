#url https://noauto-nolife.com/post/startup-django/

from textwrap import indent
from django.shortcuts import render

# Create your views here.
from django.views import View

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "bbs/index.html")

index = IndexView.as_view()
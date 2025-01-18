from django.shortcuts import render
from django.views import generic
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from .models import Bgbuild

# Create your views here.
class BgbuildList(generic.ListView):
    queryset = Bgbuild.objects.all().order_by("-created_on")
    template_name = "bgbuild/bgbuild_list.html"

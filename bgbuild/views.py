from django.shortcuts import render
from django.views import generic
from .models import Bgbuild

# Create your views here.
class BgbuildList(generic.ListView):
    model = Bgbuild
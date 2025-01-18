from django.shortcuts import render
from django.views import generic
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.db.models import Q
from .models import Bgbuild

# Create your views here.
class BgbuildList(generic.ListView):
    queryset = Bgbuild.objects.all().order_by("-created_on")
    template_name = "bgbuild/bgbuild_list.html"

def searchBuild(request):
    if request.method == "POST":
        build_search = request.POST.get('searchbuilds')
        builds = Bgbuild.objects.filter(bgbase_class__contains=build_search) | Bgbuild.objects.filter(bgbuild_role__contains=build_search)
        total = builds.count()
        return render(request, 'bgbuild/bgbuild_search.html', {'build_search': build_search, 'builds':builds, 'total': total,})
    else:
        return render(request, 'bgbuild/bgbuild_search.html', {})


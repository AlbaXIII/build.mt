from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.db.models import Q
from .models import Bgbuild
from .forms import BgcommentForm


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

def buildDetail(request, slug):
    queryset = Bgbuild.objects.filter(status=1)
    build = get_object_or_404(queryset, slug=slug)
    comments = build.comments.all().order_by("-created_on")
    comment_count = build.comments.count()

    if request.method == "POST":
        comment_form = BgcommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.build = build
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted!'
            )

    comment_form = BgcommentForm()

    return render(
        request,
        "bgbuild/bgbuild_detail.html",
        {
            "build": build,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )

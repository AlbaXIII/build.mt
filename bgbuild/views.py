from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.db.models import Q
from .models import Bgbuild, Bgcomment
from .forms import BgcommentForm, BgreplyForm, BgbuildForm

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
    
    if request.method == 'POST':
        comment_form = BgcommentForm(data=request.POST)
        reply_form = BgreplyForm(data=request.POST)
        if 'comment' in request.POST:
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.build = build
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment posted'
            )
        elif 'reply' in request.POST:
            comment_id = request.POST['comment_id']
            comment = Bgcomment.objects.get(id=comment_id)
            reply = reply_form.save(commit=False)
            reply.user = request.user
            reply.comment = comment
            reply.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Reply posted'
            )
            
    comment_form = BgcommentForm()
    reply_form = BgreplyForm()

    return render(
        request,
        "bgbuild/bgbuild_detail.html",
        {
            "build": build,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
            "reply_form": reply_form,
        },
    )

class BgAddBuild(generic.CreateView):

    template_name = 'bgbuild/bgbuild_add.html'
    model = Bgbuild
    form_class = BgbuildForm
    success_url = "/bgbuild/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.add_message(
            self.request,
            messages.SUCCESS,
            f'{self.request.user} - build post was successfully submitted'
        )
        response = super().form_valid(form)
        return response

class BgEditBuild(generic.UpdateView):
    template_name = 'bgbuild/bgbuild_edit.html'
    model = Bgbuild
    form_class = BgbuildForm
    success_url = '/bgbuild/'

    def test_func(self):
        return self.request.user == self.get_object().user

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        messages.add_message(
            self.request, messages.SUCCESS,
            f'{self.request.user} your build was successfully edited')
        return response

class BgDeleteBuild(generic.DeleteView):
    model = Bgbuild
    success_url = "/bgbuild/"
    success_message = 'Build successfully deleted'

    def test_func(self):
        """
        Ensure that the logged-in user is the owner of the build.
        """
        return self.request.user == self.get_object().user
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from bgbuild.models import Bgbuild

# Create your views here.


class Home(TemplateView):
    """
    Class based view to render home page.
    """
    template_name = 'core/index.html'


class UserBuilds(ListView):

    model = Bgbuild
    template_name = 'core/account.html'
    context_object_name = 'mybuilds'

    def get_queryset(self):
        """
        Return a queryset of builds created by the logged-in user,
        ordered by creation date in descending order.
        """
        return Bgbuild.objects.filter(
            user=self.request.user).order_by('-created_on')
   

class UserFavourites(ListView):

    model = Bgbuild
    template_name = 'core/favourites.html'
    context_object_name = 'myfavourites'

    def get_queryset(self):
        user = self.request.user
        queryset = user.bgbuild_favourite.all()
        return queryset



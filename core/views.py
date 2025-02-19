from django.views.generic import TemplateView, ListView
from bgbuild.models import Bgbuild
from django.contrib.auth.mixins import (
    LoginRequiredMixin
)

# Create your views here.


class Home(TemplateView):
    """
    Class based view to render home page.

    **Template:**
    :template:`core/index.html`
    """
    template_name = 'core/index.html'


class UserBuilds(LoginRequiredMixin, ListView):
    """
    Display a list of Bgbuilds created by auth.User.

    **Context**

    ``mybuilds``
        A list of :model:`bgbuild.Build` instances created by the user.

    **Template:**

    :template:`core/account.html`
    """
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


class UserFavourites(LoginRequiredMixin, ListView):
    """
    Display a list of favourited Bgbuilds created by auth.User relating
    to instances of :model:`bgbuild.Build`

    **Context**

    ``builds``
        A list of :model:`bgbuild.Build` instances created by the user.

    **Template:**

    :template:`core/favourites.html`
    """
    model = Bgbuild
    template_name = 'core/favourites.html'
    context_object_name = 'myfavourites'

    def get_queryset(self):
        user = self.request.user
        queryset = user.bgbuild_favourite.all()
        return queryset

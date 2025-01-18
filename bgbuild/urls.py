from . import views
from django.urls import path
from .views import BgbuildList, searchBuild

urlpatterns = [
    path('', BgbuildList.as_view(), name="bgbuilds"),
    path('q/', searchBuild, name='searchbuild'),
] 
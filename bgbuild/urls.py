from . import views
from django.urls import path
from .views import BgBuildList, search_build, BgAddBuild, BgEditBuild
from .views import BgDeleteBuild, BgBuildFavourite

urlpatterns = [
    path('add/', BgAddBuild.as_view(), name="bgbuildadd"),
    path('', BgBuildList.as_view(), name="bgbuilds"),
    path('search/', search_build, name='searchbuild'),
    path('<slug:slug>/', views.build_detail, name='bgbuilddetail'),
    path('edit/<slug:pk>/', BgEditBuild.as_view(), name='bgeditbuild'),
    path('delete/<slug:pk>/', BgDeleteBuild.as_view(), name='bgdeletebuild'),
    path('favourite/<slug:build_slug>/',
         BgBuildFavourite.as_view(), name="bgfavouritebuild"),
]

from . import views
from django.urls import path
from .views import BgbuildList, searchBuild, buildDetail, BgAddBuild, BgEditBuild, BgDeleteBuild

urlpatterns = [
    path('add/', BgAddBuild.as_view(), name="bgbuildadd"),
    path('', BgbuildList.as_view(), name="bgbuilds"),
    path('q/', searchBuild, name='searchbuild'),
    path('<slug:slug>/', views.buildDetail, name='bgbuilddetail'),
    path('delete/<slug:pk>/', BgDeleteBuild.as_view(), name='bgdeletebuild'),
    path("edit/<slug:pk>/", BgEditBuild.as_view(), name="bgeditbuild"),
] 
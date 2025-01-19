from . import views
from django.urls import path
from .views import BgbuildList, searchBuild, buildDetail

urlpatterns = [
    path('', BgbuildList.as_view(), name="bgbuilds"),
    path('q/', searchBuild, name='searchbuild'),
    path('<slug:slug>/', views.buildDetail, name='bgbuilddetail'),
] 
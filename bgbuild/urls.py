from . import views
from django.urls import path
from .views import BgbuildList, searchBuild, buildDetail, bgcommentEdit, BgAddBuild

urlpatterns = [
    path('add/', BgAddBuild.as_view(), name="bgbuildadd"),
    path('', BgbuildList.as_view(), name="bgbuilds"),
    path('q/', searchBuild, name='searchbuild'),
    path('<slug:slug>/', views.buildDetail, name='bgbuilddetail'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.bgcommentEdit, name='comment_edit'),
] 
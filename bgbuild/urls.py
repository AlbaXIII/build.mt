from . import views
from django.urls import path

urlpatterns = [
    path('', views.BgbuildList.as_view(), name='bgbuild'),
]
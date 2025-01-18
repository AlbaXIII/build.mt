from . import views
from django.urls import path
from .views import BgbuildList

urlpatterns = [
    path('', BgbuildList.as_view(), name="bgbuilds"),
]
from django.urls import path
from .views import Home, UserBuilds

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('account/', UserBuilds.as_view(), name='account')
]
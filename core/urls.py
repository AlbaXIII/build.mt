from django.urls import path
from .views import Home, UserBuilds, UserFavourites

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('account/', UserBuilds.as_view(), name='account'),
    path('favourites/', UserFavourites.as_view(), name='favourites'),
]

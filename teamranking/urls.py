
from django.urls import path
from . import views


urlpatterns = [
    path('',views.Standings.as_view(),name='TeamStandings'),
]


from django.urls import path
from . import views


urlpatterns = [
    path('updaterating',views.FileUpload.as_view(),name="FileUpload"),
    path('vjudgestandings',views.vjudgeContestStandings,name="vjudgeStandings"),
]

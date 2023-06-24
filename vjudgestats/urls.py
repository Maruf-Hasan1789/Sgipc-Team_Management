
from django.urls import path
from . import views


urlpatterns = [
    path('vjudgestats',views.FileUpload.as_view(),name="FileUpload"),
    path('recentconteststandings',views.recentconteststandings),
]
